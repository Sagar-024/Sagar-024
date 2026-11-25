#!/usr/bin/env python3
"""
Auto-update the README work line with live HFlow counts.
Injects one line between <!-- HFLOW:START --> and <!-- HFLOW:END -->.
"""
import os, re, json, urllib.request, urllib.parse

TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
REPO = "Hebbian-Robotics/hflow"
AUTHOR = "Sagar-024"
HEADERS = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"


def gh_search_count(q):
    params = urllib.parse.urlencode({"q": q, "per_page": 1})
    url = f"https://api.github.com/search/issues?{params}"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read().decode())
        return data.get("total_count", 0)


pr_count = gh_search_count(f"repo:{REPO} author:{AUTHOR} is:pr is:merged")
issue_count = gh_search_count(f"repo:{REPO} author:{AUTHOR} is:issue")

block = f"**{pr_count} PRs merged, {issue_count} issues opened** in [{REPO}](https://github.com/{REPO})."

readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

start = "<!-- HFLOW:START -->"
end = "<!-- HFLOW:END -->"
pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
replacement = f"{start}\n\n{block}\n\n{end}"

if start not in content or end not in content:
    raise SystemExit(f"Markers {start}/{end} not found in README.md")

new_content, n = pattern.subn(replacement, content)
if n == 0:
    raise SystemExit("Pattern replace failed")

if new_content == content:
    print("No change. README already up to date")
else:
    with open(readme_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_content)
    print(f"Updated README: {pr_count} PRs, {issue_count} issues")
