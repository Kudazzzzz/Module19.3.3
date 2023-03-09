import requests
import json
import pytest
status = 'available'
base_url = 'https://petstore.swagger.io/v2'
res_get = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers={'accept': 'application/json'})
print('Статус код запроса GET', res_get.status_code)
print(res_get.text)
print(res_get.json())
print(type(res_get.json()))

input_pet = {
        "id": 1234,
        "category": {
            "id": 23,
            "name": "Pes"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 7,
                "name": "Dog"
            }
        ],
        "status": "available"
    }
headr = {'accept': 'application/json', 'Content-Type': 'application/json'}

res_post = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=headr )
print('Статус код запроса POST', res_post.status_code)
print(res_post.text)
print(res_post.json())
print(type(res_post.json()))

input_pet_put = {
        "id": 1234,
        "category": {
            "id": 23,
            "name": "Koz"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 7,
                "name": "Dog"
            }
        ],
        "status": "available"
    }
res_put = requests.put(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet_put), headers=headr )
print('Статус код запроса PUT', res_put.status_code)
print(res_put.text)
print(res_put.json())

res_delete = requests.delete(url='https://petstore.swagger.io/v2/pet/1234', headers=headr)
print('Статус код запроса DELETE', res_delete.status_code)
