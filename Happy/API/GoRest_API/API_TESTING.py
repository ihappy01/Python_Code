import requests
import random
import json
import string

#base url
base_url ="https://gorest.co.in"

auth_token ="Bearer ee0bb76d1b52fc92ffb03fe33bc479e3f520c4b4cd0eae37fc2a5cb225dc5297"

#GET Request
def get_request():
    url = base_url+"/public/v2/users"
    print("Get url:", url)
    header ={'Authorization': auth_token}
    response = requests.get(url,headers=header)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data,indent=4)
    print("Json GET body response:",json_str)

    #POST Request
def post_request():
    url = base_url+"/public/v2/users"
    print("POST url:", url)
    header ={'Authorization': auth_token}
    data =  {
        "name": "indrajeet1",
        "email": "indrajeet12@gmail.com",
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url,json=data,headers=header)
    print("Response status is: ",response.status_code)
    assert response.status_code==201

    json_data= response.json()
    json_str = json.dumps(json_data,indent=4)
    print("Json POST body response:",json_str)
    user_id = json_data['id']
    print(user_id)
    assert 'name' in json_data
    assert json_data['name']== "indrajeet1"
    return user_id


#PUT Request
def put_request(user_id):
    url =base_url+f"/public/v2/users/{user_id}"
    print("Put url:", url)
    header = {'Authorization': auth_token}
    data = {
        "name": "indrajeet lab",
        "email": "indrajeet_lab@gmail.com",
        "gender": "male",
        "status": "inactive"
    }

    response= requests.put(url,headers=header,json=data)
    print("PUT Response status is: ", response.status_code)
    assert response.status_code == 200

    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("Json PUT body response:", json_str)

    assert json_data['id']== user_id
    assert json_data['name'] == "indrajeet lab"

#DELETE Request
def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("Delete url:", url)
    header = {'Authorization': auth_token}

    response = requests.delete(url,headers=header)
    assert response.status_code == 204
    print("..........DELETE USER IS DONE......")




#Call
# get_request()
user_id = post_request()
# put_request(user_id)
delete_request(user_id)