from sanic import Sanic

import config
from methods import status, products
import middleware
import services
import logging


def main():
    app = Sanic('product-api')

    # Infrastructure
    app.blueprint(middleware.bp)
    app.blueprint(services.bp)

    # Methods
    app.blueprint(products.bp)
    app.blueprint(status.bp)

    # Services
    app.blueprint(services.product_storage.bp)

    # Set root logging level
    logging.getLogger().setLevel(logging.INFO)

    app.run(host='0.0.0.0', port=config.LISTEN_PORT)


if __name__ == "__main__":
    main()
