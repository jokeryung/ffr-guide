"""Build the guide from design/prototype.html + research/data.json.

Outputs:
  site/index.html  - page body for the claude.ai Artifact (the Artifact wrapper adds <head> basics)
  docs/index.html  - standalone page for GitHub Pages / opening locally

Re-run after updating data.json or prototype.html:  python3 -I build.py"""
import json, os, re, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))

data = json.load(open(os.path.join(ROOT, "research/data.json"), encoding="utf-8"))

# Short UI labels; full term names stay in REPORT.md.
data["meta"]["terms"] = {"phantom": "幻兵", "stage": "MR", "awakening": "覺醒"}
data["meta"]["server"] = "單機版"
data["meta"]["gameVersion"] = "1.0"

# Assets ship next to the page: research/assets/x -> assets/x
for group in ("characters", "phantoms"):
    for item in data[group]:
        img = item.get("image") or {}
        if img.get("local"):
            img["local"] = img["local"].replace("research/assets/", "assets/", 1)

page = open(os.path.join(ROOT, "design/prototype.html"), encoding="utf-8").read()
blob = json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/")
page, n = re.subn(r'(<script id="guide-data" type="application/json">)(.*?)(</script>)',
                  lambda m: m.group(1) + "\n" + blob + "\n" + m.group(3), page, count=1, flags=re.S)
assert n == 1, "guide-data block not found"

STANDALONE_HEAD = '<!doctype html>\n<html lang="zh-Hant">\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'

for out, html in (("site", page), ("docs", STANDALONE_HEAD + page)):
    out_dir = os.path.join(ROOT, out)
    os.makedirs(out_dir, exist_ok=True)
    if os.path.exists(os.path.join(out_dir, "assets")):
        shutil.rmtree(os.path.join(out_dir, "assets"))
    shutil.copytree(os.path.join(ROOT, "research/assets"), os.path.join(out_dir, "assets"))
    open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8").write(html)

print("built", len(data["characters"]), "characters,", len(data["phantoms"]), "phantoms,", len(data["builds"]), "builds")
