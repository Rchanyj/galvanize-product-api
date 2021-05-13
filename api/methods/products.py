from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, json

bp = Blueprint('products')


@bp.get('/product/<id:int>')
def get_product(request: Request, id: int) -> HTTPResponse:
    product_storage = request.app.services.product_storage
    try:
        product_data = product_storage.get_product(id)
    except Exception:
        raise Exception('Error returning product')

    product = {
        'id': product_data[0],
        'name': product_data[1],
        'price': product_data[2],
        'description': product_data[3],
        'view_count': product_data[4]
    }

    return json(product)
