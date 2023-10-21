import json

import requests

# API URL
url="https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url)

print(response.status_code)
res=json.loads(response.content)
print(res)
print(type(res))
print(res['page'])
print(res['data'][0]['email'])
print(response.headers)


