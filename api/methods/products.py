from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, json
import requests

import urllib.parse as urlparse
from urllib.parse import parse_qs
from decimal import Decimal

import config
import logging

bp = Blueprint('products')


@bp.post('/product/new')
def create_product(request: Request) -> HTTPResponse:
    product_storage = request.app.services.product_storage
    product_data = request.json
    try:
        product_storage.create_product(product_data)
    except Exception:
        raise Exception('Failed to create product')

    return HTTPResponse(status=204)


@bp.get('/product/<id:int>')
def get_product(request: Request, id: int) -> HTTPResponse:
    product_storage = request.app.services.product_storage
    try:
        product_data = product_storage.get_product(id)
    except Exception:
        raise Exception('Error returning product')

    price = product_data[2]

    query_params = get_query_params(request.url)
    currency_param = query_params.get('currency', None)
    if currency_param:
        currency = currency_param[0]
        payload = {
            'access_key': config.CURRENCY_API_KEY,
            'currencies': currency,
            'format': 1
        }
        try:
            resp = requests.get(config.CURRENCY_API_ENDPOINT, params=payload)
            curr_data = resp.json()
            curr_conversion = curr_data['quotes'][f'USD{currency}']
            price = round(product_data[2]*curr_conversion, 2)
        except Exception:
            logging.info('Error in converting currency; returning default USD')

    product = {
        'id': product_data[0],
        'name': product_data[1],
        'price': price,
        'description': product_data[3],
        'view_count': product_data[4]
    }

    return json(product)


def get_query_params(url):
    parsed = urlparse.urlparse(url)
    parsed_query = parse_qs(parsed.query)
    return parsed_query
