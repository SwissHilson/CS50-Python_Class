import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

results= response.json()
for result in results["results"]:
    print(result["trackName"])


#print(json.dumps(response.json(), indent=2))