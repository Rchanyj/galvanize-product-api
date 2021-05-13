from sanic import Blueprint
import psycopg2
from tenacity import retry, stop_after_attempt, wait_fixed

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
    logging.info('Closing product storage...')

    product_storage = app.services.product_storage
    if product_storage:
        product_storage.close()


# Queries:
sql_fetch_product = '''select *
                        from products
                        where id = %s
                        and active = true'''

sql_increment_views = '''update products
                        set view_count = %s
                        where id = %s'''

sql_create_product = '''insert into products
                        values (nextval('product_id_seq'), %s, %s, %s, 0, true)'''

sql_fetch_most_viewed = '''select *
                        from products
                        where view_count > 0
                        and active = true
                        order by view_count desc
                        limit %s'''

sql_deactivate_product = '''update products
                        set active = false
                        where id = %s'''


class ProductStorage:
    def __init__(self):
        self.conn = None
        self.cursor = None

    @retry(reraise=True, stop=stop_after_attempt(2), wait=wait_fixed(1))
    def init(self):
        try:
            self.conn = psycopg2.connect(config.PG_CONNECTION_STRING)
            self.cursor = self.conn.cursor()
        except Exception:
            raise Exception('Failed to connect to db')

    def create_product(self, product_data):
        logging.info('Creating product...')
        try:
            self.cursor.execute(sql_create_product,
                                (product_data.get('name'),
                                 product_data.get('price'),
                                 product_data.get('description')))
        except Exception:
            raise Exception('Failed to create product')

    def get_product(self, id):
        logging.info('Fetching product...')
        try:
            self.cursor.execute(sql_fetch_product, (id,))
            product = self.cursor.fetchone()
            self.increment_views(id, product[4]+1)
            return product
        except Exception:
            logging.exception('Failed to get product')
            return {}

    def get_most_viewed(self, limit=5):
        logging.info('Fetching most viewed...')
        try:
            self.cursor.execute(sql_fetch_most_viewed, (limit,))
            products = self.cursor.fetchall()
            return products
        except Exception:
            logging.exception('Failed to get products')
            return {}

    def deactivate_product(self, id):
        logging.info(f'Deactivating product {id}...')
        try:
            self.cursor.execute(sql_deactivate_product, (id,))
        except Exception:
            raise Exception('Failed to deactivate product')

    def increment_views(self, id, views):
        logging.info(f'Incrementing views for product {id}...')
        try:
            self.cursor.execute(sql_increment_views, (views, id))
        except Exception:
            raise Exception('Failed to increment views')

    def close(self):
        if self.conn:
            self.conn.close()

