"""Anonymous acceptance matrix; standard library only, no credentials or model calls."""

import json
import html
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ENDPOINT = "https://api.revenirdata.com/radarjobs/mcp"
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs/plugin-publication/search-evidence.json"
HEADERS = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
TARGET_OPPORTUNITY_ID = "3f5785c2-0378-4896-ae1a-8b297a48bbd4"
sequence = 0


def rpc(method, params):
    global sequence
    sequence += 1
    body = json.dumps({"jsonrpc": "2.0", "id": sequence, "method": method, "params": params}).encode()
    started = time.perf_counter()
    request = urllib.request.Request(ENDPOINT, data=body, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=40) as response:
        value = json.load(response)
        status = response.status
    return {"status": status, "latency_ms": round((time.perf_counter() - started) * 1000),
            "response": value}


def call(name, arguments):
    return rpc("tools/call", {"name": name, "arguments": arguments})


CASES = [
    ("Remote 1099 senior data engineering", {"remote": True, "engagement_model": ["1099"],
     "level": ["senior"], "job_subfamily": ["data_engineering"]}),
    ("C2C Snowflake contracts", {"engagement_model": ["c2c"], "title_contains": "Snowflake"}),
    ("Remote AI engineer contracts", {"remote": True, "job_class": ["ai_engineer"]}),
    ("Contracts at least 50 USD/hour", {"rate_min": 50, "currency": "USD"}),
    ("Forward deployed or AI engineer", {"title_contains": "forward deployed engineer",
     "job_class": ["ai_engineer"], "match_mode": "closest"}),
    ("Intentional zero results", {"title_contains": "zzradarjobsacceptancezeromatchzz"}),
    ("Malformed unsupported skills field", {"skills": ["Snowflake"]}),
    ("Permanent non-contract nursing", {"engagement_model": ["permanent"], "job_class": ["nurse"]}),
]


def verify_links(evidence):
    jobs = [case["response"]["result"]["structuredContent"]["jobs"][0]
            for case in evidence["cases"][:5]]
    evidence["detail"] = call("get_contract_job", {"opportunity_id": jobs[0]["id"]})
    detail = evidence["detail"]["response"]["result"]
    assert not detail.get("isError")
    assert detail["structuredContent"]["job"]["id"] == jobs[0]["id"]
    evidence["result_links"] = []
    for job in {job["id"]: job for job in jobs}.values():
        started = time.perf_counter()
        with urllib.request.urlopen(job["radarjobs_url"], timeout=40) as response:
            body = html.unescape(response.read().decode())
            assert response.status == 200 and job["id"] in response.url
            assert job["title"] in body and "Try RadarJobs" in body
            evidence["result_links"].append({"status":response.status,"url":response.url,
                "opportunity_id":job["id"],"title_verified":True,
                "latency_ms":round((time.perf_counter()-started)*1000)})
            print(f"Result link: {response.status} {job['title']}")
    evidence["links_checked_at"] = datetime.now(timezone.utc).isoformat()
    for name, url in [("backend","https://api.revenirdata.com/readyz"),
                      ("website","https://www.revenirdata.com/api/build")]:
        with urllib.request.urlopen(url,timeout=20) as response:
            evidence[name + "_deployment"] = json.load(response)
    OUTPUT.write_text(json.dumps(evidence, indent=2), encoding="utf-8")


def verify_engagement_resolution(evidence):
    common = {"title_contains": "Snowflake AWS Redshift"}
    strict_1099 = call(
        "search_contract_jobs",
        {"filters": {**common, "engagement_model": ["1099"]}, "limit": 5},
    )
    w2 = call(
        "search_contract_jobs",
        {"filters": {**common, "engagement_model": ["w2_contract"]}, "limit": 5},
    )
    detail = call("get_contract_job", {"opportunity_id": TARGET_OPPORTUNITY_ID})
    strict_jobs = strict_1099["response"]["result"]["structuredContent"]["jobs"]
    w2_jobs = w2["response"]["result"]["structuredContent"]["jobs"]
    target = detail["response"]["result"]["structuredContent"]["job"]
    assert TARGET_OPPORTUNITY_ID not in {job["id"] for job in strict_jobs}
    assert TARGET_OPPORTUNITY_ID in {job["id"] for job in w2_jobs}
    assert target["engagement_models"] == ["w2_contract"]
    assert target["engagement_resolution"] == {
        "status": "restricted",
        "excluded_models": ["1099", "c2c"],
        "conflicting_models": ["1099"],
        "evidence_labels": ["w2_positive"],
    }
    evidence["engagement_resolution_regression"] = {
        "opportunity_id": TARGET_OPPORTUNITY_ID,
        "strict_1099": strict_1099,
        "w2_contract": w2,
        "detail": detail,
    }


def main():
    if sys.argv[1:] == ["--links-only"]:
        verify_links(json.loads(OUTPUT.read_text(encoding="utf-8")))
        return
    evidence = {"checked_at": datetime.now(timezone.utc).isoformat(), "endpoint": ENDPOINT,
                "authentication": "none", "cases": []}
    evidence["initialize"] = rpc("initialize", {"protocolVersion": "2025-11-25", "capabilities": {},
        "clientInfo": {"name": "radarjobs-acceptance", "version": "1.0.0"}})
    evidence["tools"] = rpc("tools/list", {})
    tools = evidence["tools"]["response"]["result"]["tools"]
    assert {t["name"] for t in tools} == {
        "search_contract_jobs", "get_contract_job", "get_contract_job_taxonomy"}
    evidence["taxonomy"] = call("get_contract_job_taxonomy", {"parent_id": "data"})
    first_job = None
    for index, (name, filters) in enumerate(CASES):
        result = call("search_contract_jobs", {"filters": filters, "limit": 5})
        payload = result["response"]["result"]
        error = payload.get("isError", False)
        if index >= 6:
            assert error, f"Expected a validation error: {name}"
        else:
            assert not error, f"Unexpected tool error: {name}: {payload}"
            data = payload["structuredContent"]
            assert data["returned"] == len(data["jobs"]) <= 5
            if index < 5:
                assert data["returned"] > 0, f"Starter needs real inventory: {name}"
            for job in data["jobs"]:
                assert job["liveness_status"] == "live"
                link = urllib.parse.urlsplit(job["radarjobs_url"])
                assert link.scheme == "https" and link.netloc == "www.revenirdata.com"
                assert urllib.parse.parse_qs(link.query)["utm_campaign"] == ["radarjobs_codex"]
                if filters.get("engagement_model"):
                    assert set(filters["engagement_model"]) & set(job["engagement_models"])
                if filters.get("remote"):
                    assert job["location"]["remote"] is True
                if "rate_min" in filters:
                    rate = job["rate"]
                    assert rate["currency"] == "USD" and rate["unit"] == "hour"
                    assert float(rate["minimum"]) >= filters["rate_min"]
                first_job = first_job or job
            if index == 5:
                assert data["returned"] == 0
            if index == 4 and data["relaxed_filters"]:
                assert data["relaxed_filters"] == ["title_contains"]
                assert data["applied_filters"]["job_class"] == ["ai_engineer"]
        evidence["cases"].append({"name": name, "arguments": {"filters": filters, "limit": 5}, **result})
        returned = payload.get("structuredContent", {}).get("returned")
        print(f"{name}: status={result['status']} error={error} returned={returned} {result['latency_ms']}ms")
        OUTPUT.write_text(json.dumps(evidence, indent=2), encoding="utf-8")
    verify_engagement_resolution(evidence)
    verify_links(evidence)
    print(f"Saved actual public responses: {OUTPUT}")


if __name__ == "__main__":
    main()
