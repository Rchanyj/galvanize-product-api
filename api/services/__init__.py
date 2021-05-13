import logging

from sanic import Blueprint

from services.product_storage import ProductStorage

bp = Blueprint('services')


@bp.listener('before_server_start')
def attach(app, _):
    logging.info('Initializing external dependencies layer')
    app.services = ExternalDependencies()


class ExternalDependencies:
    product_storage: ProductStorage
