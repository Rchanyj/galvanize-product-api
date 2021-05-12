import os

LISTEN_PORT = int(os.getenv('LISTEN_PORT', 8080))
PG_CONNECTION_STRING = int(os.getenv('PG_CONNECTION_STRING', 'dbname=DemoProducts user=postgres'))
