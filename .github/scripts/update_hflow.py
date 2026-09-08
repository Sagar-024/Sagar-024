#!/usr/bin/env python3
"""
Auto-update README top section with live HFlow stats.
Fetches 23 merged PRs / 8 issues etc and injects between <!-- HFLOW:START --> and <!-- HFLOW:END -->
"""
import os, re, json, urllib.request, urllib.parse

TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
REPO = "Hebbian-Robotics/hflow"
AUTHOR = "Sagar-024"
HEADERS = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"

def gh_search(q, per_page=5):
    # use search/issues endpoint
    params = urllib.parse.urlencode({"q": q, "per_page": per_page, "sort": "updated", "order": "desc"})
    url = f"https://api.github.com/search/issues?{params}"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read().decode())
        return data.get("total_count", 0), data.get("items", [])

def gh_search_count(q):
    # only count, per_page=1 to minimize
    params = urllib.parse.urlencode({"q": q, "per_page": 1})
    url = f"https://api.github.com/search/issues?{params}"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read().decode())
        return data.get("total_count", 0)

# counts
pr_count = gh_search_count(f"repo:{REPO} author:{AUTHOR} is:pr is:merged")
issue_count = gh_search_count(f"repo:{REPO} author:{AUTHOR} is:issue")

_, prs = gh_search(f"repo:{REPO} author:{AUTHOR} is:pr is:merged", per_page=5)
_, issues = gh_search(f"repo:{REPO} author:{AUTHOR} is:issue", per_page=3)

# Build markdown block
# Keep curated descriptions map for known PRs to preserve your hand-written context
DESC = {
    457: "verify delivered snapshots against integrity receipts — catch bit-rot in landing",
    429: "CRC-validate reused landing episodes before stamping receipts — close resume-path corruption gap",
    411: "cover completeness knobs in the check-version contract — prevent version aliasing",
    403: "stop stamping success=true on episodes the source marked as failures; read the collector's own outcome label",
    389: "every delivered episode carries its content hash, so a damaged delivery is detectable from the receipt alone",
    373: "enforce a video safety invariant that earlier code only trusted, closing a silent decode-loss path",
    354: "31x faster scans on the canonical write path, byte-identical output",
    345: "reject input streams where remux drops the reorder tail, preventing downstream decode failures",
}

def pr_line(pr):
    n = pr["number"]
    title = pr["title"]
    url = pr["html_url"]
    # extract type from title for cleaner label
    desc = DESC.get(n, title)
    # shorten desc if too long
    if len(desc) > 120:
        desc = desc[:117] + "..."
    # use first word as tag e.g., fix/import
    # try to keep title's prefix like fix(import): ...
    short = title.split(":")[0] if ":" in title else title[:20]
    return f"- **#{n}** [{title}]({url}): {desc}"

def issue_line(iss):
    n = iss["number"]
    title = iss["title"]
    url = iss["html_url"]
    state = iss["state"]
    # short desc from title
    return f"- **#{n}** [{title}]({url}) — {state}"

block = f"""**{pr_count} PRs merged, {issue_count} issues opened** in [Hebbian-Robotics/hflow](https://github.com/Hebbian-Robotics/hflow) so far. Highlights:

"""
for pr in prs:
    block += pr_line(pr) + "\n"
block += "\nIssues I opened:\n\n"
for iss in issues:
    block += issue_line(iss) + "\n"
block += "\n[See all my merged PRs in HFlow](https://github.com/Hebbian-Robotics/hflow/pulls?q=is%3Apr+author%3ASagar-024+is%3Aclosed)"

# Patch README
readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

start = "<!-- HFLOW:START -->"
end = "<!-- HFLOW:END -->"
pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
replacement = f"{start}\n\n{block}\n\n{end}"

if start not in content or end not in content:
    raise SystemExit(f"Markers {start}/{end} not found in README.md — add them around the Currently section")

new_content, n = pattern.subn(replacement, content)
if n == 0:
    raise SystemExit("Pattern replace failed")

if new_content == content:
    print("No change — README already up to date")
else:
    with open(readme_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_content)
    print(f"Updated README: {pr_count} PRs, {issue_count} issues, {len(prs)} PR highlights, {len(issues)} issues")
