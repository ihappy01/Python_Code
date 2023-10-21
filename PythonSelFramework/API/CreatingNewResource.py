import json

import jsonpath as jsonpath
import requests

url = "https://reqres.in/api/users"

#Read Input Json File

file =open("D:\\Test_Data\\API\\CreateUser_json.json",'r')
json_input = file.read()
request_json = json.loads(json_input)

print(request_json)

# Make Post request with json Input body

response = requests.post(url,request_json)
print(response.content)

#Validating Response Code
assert response.status_code == 201

# Fetch header from response
print(response.headers)
print(response.headers.get('Connection'))

# Parse response to Json Format\
response_json = json.loads(response.text)

# Pick Id using JsoN path
id = jsonpath.jsonpath(response_json,'id')
print(id[0])
