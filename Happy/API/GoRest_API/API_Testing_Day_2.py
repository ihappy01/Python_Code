import requests
import json
import random


base_url = "https://gorest.co.in"
#Auth_token
token_id = "Bearer ee0bb76d1b52fc92ffb03fe33bc479e3f520c4b4cd0eae37fc2a5cb225dc5297"

#GET Method
def get_request():
    url = base_url + "/public/v2/users"
    print("Get Url:",url)
    headers={"Authorization":token_id}
    response = requests.get(url,headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_str = json.dumps(json_data,indent=4)
    print("Get response body",json_str)
    print(json_data[1]["name"])
    print("..............Get request is Done.............")
    print("===============================================")

#POST Method
def post_request():
    url= base_url+"/public/v2/users"
    print("Post url:",url)
    headers={"Authorization":token_id}
    data={
        "id":"1234",
        "name":"Shubham",
        "email":"shubham009=@gmail.com",
        "gender":"male",
        "status":"inactive"
    }
    response = requests.post(url,json=data,headers=headers)
    print(response.status_code)

    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("Post response body", json_str)

    user_id = json_data['id']
    print("usre id ====>",user_id)
    assert response.status_code == 201

    assert "name" in json_data
    assert json_data["name"] == "Shubham"
    print("............Post request is done................")
    print("===============================================")
    return user_id



#PUT Request
def put_request(used_id):
    url = base_url + f"/public/v2/users/{used_id}"
    print("Put url:", url)
    headers = {"Authorization": token_id}
    data = {
        "id": "1234",
        "name": "Shubham Kumar",
        "email": "shubham1122802@gmail.com",
        "gender": "male",
        "status": "active"
    }

    response = requests.put(url,json=data,headers=headers)
    print(response.status_code)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("Put response body", json_str)
    assert json_data["id"] == used_id
    assert json_data["name"] == "Shubham Kumar"
    print("..............Put request is Done.............")
    print("===============================================")


#Delete Request
def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("Delete url:", url)
    headers = {"Authorization": token_id}
    response = requests.delete(url,headers=headers)
    response.status_code == 204
    print("..............Delete user is Done.............")
    print("===============================================")



# get_request()
user_id =post_request()
# put_request(user_id)
# delete_request(user_id)
