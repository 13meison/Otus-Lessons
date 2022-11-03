import requests
import pytest
import random
from jsonschema import validate

dog_url = 'https://dog.ceo/api/'
api_dict = {
    'list_all': 'breeds/list/all/',
    'img_rnd': 'breeds/image/random/',
    'breed': 'breed/'
}

schema = {
    "type": "object",
    "properties": {
        "message": {'type': 'object'},
        "status": {"type": "string"},
    },
}


def _list_breeds():
    '''Функция для получения и создания  списка пород'''
    response = requests.get(dog_url + api_dict['list_all'])
    r_json = response.json()
    return list(r_json['message'].keys())


@pytest.mark.parametrize('api_url', api_dict.values())
def test_status_code(api_url):
    if api_url == 'breed/':
        api_url = api_url + 'hound/images/random'
    response = requests.get(dog_url + api_url)
    assert response.status_code == 200

@pytest.mark.parametrize('breed', _list_breeds())
def test_list_sub_breeds(breed):
    response = requests.get(dog_url + api_dict['breed'] + breed + '/list')
    assert response.status_code == 200

def test_json_method_all():
    response = requests.get(dog_url + api_dict['list_all'])
    r_json = response.json()
    validate(instance=r_json, schema=schema)


def test_all_img_for_breed():
    response = requests.get(dog_url + api_dict['breed'] + random.choice(_list_breeds()) + '/images')
    assert response.status_code == 200
    assert response.json()["status"] == "success"
