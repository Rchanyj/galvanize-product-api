from sanic import Blueprint
import psycopg2

import logging
import config


bp = Blueprint(__name__)


@bp.listener('before_server_start')
def attach(app, _):
    logging.info('Initializing product storage...')

    product_storage = ProductStorage()
    product_storage.init()
    app.services.product_storage = product_storage


@bp.listener('after_server_stop')
def detach(app, _):
    logging.info('Closing post storage...')

    product_storage = app.services.product_storage
    if product_storage:
        product_storage.close()


# Queries:
sql_fetch_product = '''select *
                        from posts
                        where id = ?'''


class ProductStorage:
    def __init__(self):
        self.conn = None

    def init(self):
        try:
            self.conn = psycopg2.connect(config.PG_CONNECTION_STRING)
        except Exception:
            raise Exception('Failed to connect to db')

    def get_product(self, id):
        logging.info('Fetching product...')
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_fetch_product, (id))
            product = cursor.fetchone()
            return product
        except Exception:
            logging.exception('get_product ---> error fetching post')
            return {}

