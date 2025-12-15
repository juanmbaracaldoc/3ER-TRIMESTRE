import requests
r = requests.get("https://randomuser.me/api/")
usuario = r.json()
print (usuario)