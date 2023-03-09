import requests
import json
status = 'available'
base_url = 'https://petstore.swagger.io/v2'
"""res_get = requests.get(f"{base_url}/pet/findByStatus?status={status}", headers={'accept': 'application/json'})
print('Статус код запроса GET', res_get.status_code)
print(res_get.text)
print(res_get.json())
print(type(res_get.json()))"""


def test_add_pet():
    input_pet = {
        "id": 9879,
        "category": {
            "id": 12,
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
    headr = {'accept: application/json', 'Content-Type: application/json'}

    res_post = requests.post(url='{base_url}/pet', data=json.dumps(input_pet), headers=headr )
    print(res_post)