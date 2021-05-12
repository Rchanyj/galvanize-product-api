from sanic import Blueprint
from sanic.request import Request
from sanic.response import json, HTTPResponse

import config

bp = Blueprint('status')


@bp.route('/status')
def status(_request: Request) -> HTTPResponse:
    return json({'status': 'OK'})


@bp.get('/swagger')
def definition(_request: Request) -> HTTPResponse:
    host = f'localhost:{config.LISTEN_PORT}'
    with open('./swagger.yml') as s:
        return HTTPResponse(body=s.read().replace('%host%', host))
