import requests
import sys

if len(sys.argv) !=2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=songs&limit=1&term=weezer" + sys.argv[1])

print(response.json())
