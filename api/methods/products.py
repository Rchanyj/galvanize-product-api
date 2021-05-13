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
        try:
            curr_converter = get_currency_converter(currency_param)
            price = round(product_data[2]*curr_converter, 2)
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


@bp.get('/product/most-viewed')
def get_most_viewed(request: Request) -> HTTPResponse:
    product_storage = request.app.services.product_storage
    query_params = get_query_params(request.url)
    limit_param = query_params.get('limit', [5])
    limit = limit_param[0]
    currency_param = query_params.get('currency', None)
    curr_converter = None
    try:
        products_data = product_storage.get_most_viewed(limit)
    except Exception:
        raise Exception('Error returning products')

    if currency_param:
        try:
            curr_converter = get_currency_converter(currency_param)
        except Exception:
            logging.info('Error in converting currency; returning default USD')

    products = []

    for data in products_data:
        price = data[2]
        if curr_converter:
            price = round(data[2] * curr_converter, 2)
        product = {
            'id': data[0],
            'name': data[1],
            'price': price,
            'description': data[3],
            'view_count': data[4]
        }
        products.append(product)

    return json(products)


def get_query_params(url):
    parsed = urlparse.urlparse(url)
    parsed_query = parse_qs(parsed.query)
    return parsed_query


def get_currency_converter(currency_param):
    currency = currency_param[0]
    payload = {
        'access_key': config.CURRENCY_API_KEY,
        'currencies': currency,
        'format': 1
    }
    try:
        resp = requests.get(config.CURRENCY_API_ENDPOINT, params=payload)
        curr_data = resp.json()
        curr_converter = curr_data['quotes'][f'USD{currency}']
        return curr_converter
    except Exception:
        raise Exception('Failed to get currency converter')
