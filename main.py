import json
import random
from pathlib import Path

with open(Path(__file__).parent / "packages.txt") as file:
    packages = [json.loads(line) for line in file if line.strip()]

pkg = random.choice(packages)
pkg["summary"] = pkg["summary"][0].lower() + pkg["summary"][1:]
print(f"PipShow: Have you ever heard of {pkg['name']}? Let me tell you! It's {pkg['summary']}")
