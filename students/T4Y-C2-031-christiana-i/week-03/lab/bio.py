from pathlib import Path
import json

with (Path(__file__).parent / "bio.json").open(encoding="utf-8") as f:
    data = json.load(f)
    print(data["name"])
    