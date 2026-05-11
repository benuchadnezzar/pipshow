import json
from concurrent.futures import ThreadPoolExecutor

import requests

TOP_PACKAGES_URL = "https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.min.json"

def fetch_summary(name):
    try:
        response = requests.get(f"https://pypi.org/pypi/{name}/json", timeout=5)
        if response.status_code == 200:
            summary = response.json()["info"]["summary"]
            if summary and summary.upper() != "UNKNOWN":
                return {"name": name, "summary": summary}
    except Exception:
        pass
    return None

data = requests.get(TOP_PACKAGES_URL).json()
package_names = [row["project"] for row in data["rows"]]

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(fetch_summary, name) for name in package_names]
    packages = [r for f in futures for r in (f.result(),) if r is not None]

with open("packages.txt", "w") as file:
    for pkg in packages:
        file.write(json.dumps(pkg) + "\n")
