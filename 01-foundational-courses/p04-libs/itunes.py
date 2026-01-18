# Example 1
import sys

import requests

if len(sys.argv) != 2:
    sys.exit()

respones = requests.get(
    "http://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(respones.json())


# Example 2
import json
import sys

import requests

if len(sys.argv) != 2:
    sys.exit()

respones = requests.get(
    "http://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(json.dumps(respones.json(), indent=2))


# Example 3
import json
import sys

import requests

if len(sys.argv) != 2:
    sys.exit()

respones = requests.get(
    "http://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
)

o = respones.json()
for result in o["results"]:
    print(result["trackName"])
