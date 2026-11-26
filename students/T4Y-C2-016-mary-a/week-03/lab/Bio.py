import json

with open("Bio.json") as f:
    data = json.load(f)
print(data["name"])