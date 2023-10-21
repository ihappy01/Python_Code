

import requests

response = requests.get("https://reqres.in/api/users/2")

print(type(response))
r=response.json()

print(r['data']['id'])



