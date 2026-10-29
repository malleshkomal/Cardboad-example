"""Inject data/dashboard_data.json into the HTML template -> docs/index.html (GitHub Pages)."""
import json
import os
import shutil

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
data = json.load(open(os.path.join(ROOT, "data", "dashboard_data.json"), encoding="utf-8"))
html = open(os.path.join(ROOT, "src", "dashboard_template.html"), encoding="utf-8").read()
html = html.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
open(os.path.join(ROOT, "docs", "index.html"), "w", encoding="utf-8").write(html)
shutil.copy(os.path.join(ROOT, "assets", "value_chain_scopes.svg"), os.path.join(ROOT, "docs", "value_chain_scopes.svg"))
print("docs/index.html written")
