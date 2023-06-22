import requests
from pprint import pprint



country = "Uzbekistan"
url = f"https://en.wikipedia.org/wiki/Artificial_intelligence"
r = requests.get(url)
pprint(r.text)
