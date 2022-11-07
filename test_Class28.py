import random
import string

import pytest
import requests
import json

import settings


def test_get_user_based_id_valid():
    url = "https://gorest.co.in/public/v2/users/4266"
    header = {
            'Authorization': 'Bearer bd6648bc9827db267da725fab6f1c7332b77ec3cce9b99745e10118116c1568d'
        }
    response = requests.get(url,header)
    assert response.status_code == 200
    result = response.json()
    assert len(result) > 0
    assert result["id"] == 4266
    assert result["name"] == "Adwitiya Bhattacharya"
    assert result["email"] == "adwitiya_bhattacharya@krajcik-fisher.com"
    assert result["gender"] == "male"
    assert result["status"] == "inactive"


# @pytest.mark.parametrize
def test_get_user_based_id_valid_multiple():
    id = 4266
    url = f"https://gorest.co.in/public/v2/users/{id}"
    header = {
            'Authorization': 'Bearer bd6648bc9827db267da725fab6f1c7332b77ec3cce9b99745e10118116c1568d'
        }
    response = requests.get(url,header)
    assert response.status_code == 200
    result = response.json()
    assert len(result) > 0
    assert result["id"] == 4266
    assert result["name"] == "Adwitiya Bhattacharya"
    assert result["email"] == "adwitiya_bhattacharya@krajcik-fisher.com"
    assert result["gender"] == "male"
    assert result["status"] == "inactive"


def test_get_invalid_user():
    url = "https://gorest.co.in/public/v2/users/42753533535"
    header = {
        'Authorization': 'Bearer bd6648bc9827db267da725fab6f1c7332b77ec3cce9b99745e10118116c1568d'
    }
    response = requests.get(url, header)
    assert response.status_code == 404
    result = response.json()
    assert result["message"] == "Resource not found"


def test_create_new_record():
    url = "https://gorest.co.in/public/v2/users/"
    header = {
              'Authorization': settings.token,
              'Content-Type': 'application/json',
              'Cookie': settings.cookie
             }

    name  = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=7))
    payload =json.dumps({
        "name": "PythonAPI",
        "email":settings.newemail,
        "gender":"male",
        "status":"active"
    })
    response = requests.post(url,headers=header,data=payload)
    assert response.status_code == 201
    result = response.json()
    assert result["id"] is not None
    assert result["email"] == settings.newemail
    assert result["gender"] == "male"
    assert result["status"] == "active"

def test_create_new_record_empty_token():
    url = "https://gorest.co.in/public/v2/users/"
    header = {
              'Authorization': "",
              'Content-Type': 'application/json',
              'Cookie': settings.cookie
             }

    name  = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=7))
    payload =json.dumps({
        "name": "PythonAPI",
        "email":settings.newemail,
        "gender":"male",
        "status":"active"
    })
    response = requests.post(url,headers=header,data=payload)
    assert response.status_code == 401
    result = response.json()
    assert result["message"] == "Authentication failed"

def test_create_new_record_invalid_token():
    url = "https://gorest.co.in/public/v2/users/"
    header = {
              'Authorization': "123",
              'Content-Type': 'application/json',
              'Cookie': settings.cookie
             }

    name  = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=7))
    payload =json.dumps({
        "name": "PythonAPI",
        "email":settings.newemail,
        "gender":"male",
        "status":"active"
    })
    response = requests.post(url,headers=header,data=payload)
    assert response.status_code == 401
    result = response.json()
    assert result["message"] == "Authentication failed"

def test_delete_valid():
    url = "https://gorest.co.in/public/v2/users/3667"
    header = {
        'Authorization': "123",
        'Content-Type': 'application/json',
        'Cookie': settings.cookie
    }
    response = requests.delete(url,header)
    assert response.status_code == 204

def test_delete_empty_token():
    url = "https://gorest.co.in/public/v2/users/3667"
    header = {
        'Authorization': "",
        'Content-Type': 'application/json',
        'Cookie': settings.cookie
    }
    response = requests.delete(url,header)
    assert response.status_code == 401

def test_delete_invalid_token2():
    url = "https://gorest.co.in/public/v2/users/3667"
    header = {
        'Authorization': "123",
        'Content-Type': 'application/json',
        'Cookie': settings.cookie
    }
    response = requests.delete(url,header)
    assert response.status_code == 401




