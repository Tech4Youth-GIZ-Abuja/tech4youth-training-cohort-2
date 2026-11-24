import json

with open("bio.json") as f:
    data = json.load(f)

    print(data)