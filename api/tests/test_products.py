import requests
import tests.test_config as config


def test_create_product():
    request_url = f'{config.ENDPOINT}/product/new'
    content = {
        'name': 'TestCreate1',
        'price': 50
    }
    response = requests.post(request_url, json=content)

    assert response.status_code == 204


def test_get_product():
    id = 2
    resp = requests.get(f'{config.ENDPOINT}/product/{id}')
    actual = resp.json()

    expected = {
        'id': 2,
        'name': 'AwesomeProduct 2',
        'price': 50,
        'description': 'Awesome product description',
        'view_count': 3
    }

    assert resp.status_code == 200
    assert actual == expected


def test_get_most_viewed():
    url = config.ENDPOINT + '/product/most-viewed'
    payload = {
        'limit': 2
    }
    resp = requests.get(url, params=payload)
    actual = resp.json()

    expected = [{
        "id": 3,
        "name": "AwesomeProduct 3",
        "price": 20,
        "description": None,
        "view_count": 4
        },
        {
        "id": 2,
        "name": "AwesomeProduct 2",
        "price": 50,
        "description": "Awesome product description",
        "view_count": 4  # View count incremented to account for test on get_product for this product
    }]

    assert resp.status_code == 200
    assert actual == expected
