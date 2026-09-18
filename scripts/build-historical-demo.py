"""Render publication interaction examples from recorded real MCP responses only."""

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUB = ROOT / "docs/plugin-publication"
evidence = json.loads((PUB / "history" / "anonymous-search-evidence.json").read_text(encoding="utf-8"))


def esc(value):
    return html.escape(str(value or "Unknown"), quote=True)


def compensation(job):
    rate = job.get("rate")
    if not rate or rate.get("minimum") is None:
        return "Pay not disclosed"
    low = f"{float(rate['minimum']):g}"
    high = f"–{float(rate['maximum']):g}" if rate.get("maximum") and rate["maximum"] != rate["minimum"] else ""
    return f"{rate.get('currency') or 'Currency unknown'} {low}{high} / {rate.get('unit') or 'period unknown'}"


for index, slug, prompt in [
    (1, "snowflake-contracts", "Find C2C Snowflake contracts."),
    (2, "remote-ai-contracts", "Find remote AI engineer contracts."),
]:
    case = evidence["cases"][index]
    result = case["response"]["result"]["structuredContent"]
    cards = []
    selected_jobs = result["jobs"][:3] if index == 1 else [result["jobs"][i] for i in (0, 1, 3)]
    for job in selected_jobs:
        source = ", ".join(s["name"] for s in job["sources"])
        company = job.get("employer") or job.get("intermediary") or "Organization not disclosed"
        role = "Employer" if job.get("employer") else "Intermediary" if job.get("intermediary") else "Organization"
        engagement = " · ".join({"c2c": "C2C", "1099": "1099", "w2_contract": "W-2 contract"}.get(value, value) for value in job["engagement_models"]) or "Contract type needs research"
        location = job["location"].get("text") or job["location"].get("country") or "Location not disclosed"
        verified = (job.get("last_verified_live_at") or "Unknown")[:10]
        cards.append(f'''<article><div class="job-top"><h2>{esc(job['title'])}</h2><span class="live">● Live</span></div>
        <div class="company">{esc(company)} <small>{role}</small></div>
        <div class="facts"><span>{esc(engagement)}</span><span>{esc(compensation(job))}</span><span>{esc(location)}</span></div>
        <div class="source">{esc(source)} · Last verified {esc(verified)}<a href="{esc(job['radarjobs_url'])}">View in RadarJobs ↗</a></div></article>''')
    relaxation = "Title broadened; AI-engineer requirement preserved." if result["relaxed_filters"] else "Exact filters preserved."
    markup = f'''<!doctype html><html lang="en"><meta charset="utf-8"><title>RadarJobs — {esc(prompt)}</title>
    <style>
    *{{box-sizing:border-box}}body{{margin:0;background:#030a14;color:#e9f3fa;font:20px/1.45 system-ui,sans-serif}}
    main{{position:relative;width:100vw;height:100vh;min-height:1000px;padding:58px 68px;background:radial-gradient(ellipse at 90% 0%,#0b343b 0%,transparent 55%),#050d19;overflow:hidden}}
    header{{display:flex;align-items:center;gap:22px;margin-bottom:36px}}header img{{width:72px;height:72px;border-radius:16px}}
    h1{{font-size:38px;letter-spacing:-1.5px;margin:0}}header p{{color:#93a8b8;margin:2px 0;font-size:19px}}
    .badge{{margin-left:auto;border:1px solid #255650;border-radius:99px;padding:9px 18px;color:#76e3c7;font-size:16px}}
    .layout{{display:grid;grid-template-columns:28% 1fr;gap:44px}}.eyebrow{{font-size:13px;letter-spacing:2.2px;color:#6ed9c5;text-transform:uppercase}}
    .prompt{{font-size:31px;line-height:1.32;letter-spacing:-.7px;margin:19px 0 27px}}.label{{color:#91a7b8;font-size:17px}}
    .pill{{display:inline-block;border:1px solid #244455;border-radius:8px;margin:9px 7px 0 0;padding:7px 12px;font-size:15px;color:#b7d1df}}
    aside .note{{margin-top:35px;border-top:1px solid #1c3341;padding-top:25px;font-size:18px;color:#a6bdcb}}
    .result-heading{{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;font-size:16px;color:#93a8b8}}
    .result-heading strong{{font-size:22px;color:#e9f3fa}}article{{min-height:21vh;background:#0c1927;border:1px solid #203646;border-radius:16px;margin-bottom:15px;padding:23px 26px}}
    .job-top{{display:flex;align-items:start;gap:16px}}h2{{font-size:22px;line-height:1.28;letter-spacing:-.25px;margin:0;flex:1}}
    .live{{color:#6de5bf;font-size:14px;white-space:nowrap;padding-top:3px}}.company{{font-size:17px;color:#aec4d3;margin:9px 0 14px}}small{{font-size:12px;margin-left:8px;color:#6d8a9e}}
    .facts{{display:flex;flex-wrap:wrap;gap:7px 18px;font-size:16px;color:#d5e5ed}}.facts span+span{{border-left:1px solid #2d485a;padding-left:18px}}
    .source{{border-top:1px solid #1d3344;padding-top:13px;margin-top:17px;font-size:13px;color:#7793a8;display:flex;justify-content:space-between;gap:12px}}
    a{{color:#70dfc6;text-decoration:none;white-space:nowrap}}footer{{position:absolute;bottom:40px;left:68px;right:68px;display:flex;justify-content:space-between;color:#6f8a9f;font-size:13px}}
    </style><main><header><img src="../../../plugins/radarjobs/assets/logo.png" alt="Revenir logo"><div><h1>RadarJobs</h1><p>Contract tech opportunities, across sources.</p></div><div class="badge">No account or API key needed</div></header>
    <div class="layout"><aside><div class="eyebrow">Example interaction · real inventory</div><p class="prompt">“{esc(prompt)}”</p>
    <p class="label">{esc(relaxation)}</p><span class="pill">Contract technology</span><span class="pill">Current public evidence</span>
    <div class="note">Rates stay unknown when not disclosed. Remote does not mean worldwide. Contract eligibility comes from source evidence.</div>
    <div class="note">Open a result in RadarJobs for the next step.<br><a href="https://www.revenirdata.com/radar/jobs">revenirdata.com/radar/jobs ↗</a></div></aside>
    <section><div class="result-heading"><strong>{result['returned']} live matches returned</strong><span>Showing {min(3,result['returned'])} · {case['latency_ms']} ms</span></div>{''.join(cards)}</section></div>
    <footer><span>Recorded {esc(evidence['checked_at'][:10])} · Current primary-source evidence · Availability can change</span><span>Illustrated tool response, not a Codex UI screenshot</span></footer></main></html>'''
    (PUB / "screenshots").mkdir(exist_ok=True)
    (PUB / "screenshots" / f"{slug}.html").write_text(markup, encoding="utf-8")
    print(slug, result["returned"])
