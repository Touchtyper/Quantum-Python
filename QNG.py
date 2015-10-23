import requests 
import json

url = requests.get("https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint8")
url.text

data = json.loads(url.text)

print data['data']


