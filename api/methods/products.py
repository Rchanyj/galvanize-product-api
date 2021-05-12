from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, json

bp = Blueprint('products')


@bp.get('/product/<id:int>')
def get_product(request: Request, id: int) -> HTTPResponse:
    product_storage = request.app.services.product_storage
    try:
        product = product_storage.get_product(id)
    except Exception:
        raise Exception('Error returning product')

    return json(product)
