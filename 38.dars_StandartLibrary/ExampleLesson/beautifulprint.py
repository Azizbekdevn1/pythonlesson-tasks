from pprint import pprint
import json


filename = "bemor.json"
with open(filename) as f:
    bemor = json.load(f)

print(bemor)
pprint(bemor)
