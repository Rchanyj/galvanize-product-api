from sanic import Sanic
import config
from methods import status


def main():
    app = Sanic('product-api')

    # Methods
    app.blueprint(status.bp)

    app.run(host='0.0.0.0', port=config.LISTEN_PORT)


if __name__ == "__main__":
    main()
