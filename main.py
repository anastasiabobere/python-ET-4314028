import requests
import json
z = requests.get("https://catfact.ninja/fact")
data = z.json()
print(data["fact"])