import pytest
import requests
import json
import properties

url = properties.get_settings()['URL-BASE']
files = properties.get_settings()['JSON-FILES']

def test_listUser():
    response = requests.get(url +"2")
    print("Código: "+str(response.status_code))
    print("Corpo: "+str(response.content))
    assert response.status_code == 200

def test_createUser():
    file = open(files+'create.json','r')
    json_input = file.read()
    request_json = json.loads(json_input)
	
    response = requests.post(url, request_json)
    print("Código: "+str(response.status_code))
    print("Corpo: "+str(response.content))
    assert response.status_code == 201

def test_updateUser():
    
    file = open(files+'update.json','r')
    
    json_input = file.read()
    request_json = json.loads(json_input)


    response = requests.put(url+"2",request_json)
    print("Código: "+str(response.status_code))
    print("Corpo: "+str(response.content))
    assert response.status_code == 200

def test_deleteUser():
    response = requests.delete(url+"2")
    print("Código: "+str(response.status_code))
    print("Corpo: "+str(response.content))
    assert response.status_code == 204