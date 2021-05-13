import os

LISTEN_PORT = int(os.getenv('LISTEN_PORT', 8080))
PG_CONNECTION_STRING = os.getenv('PG_CONNECTION_STRING', 'dbname=DemoProducts host=postgres port=5432 user=postgres sslmode=disable')
CURRENCY_API_KEY = os.getenv('CURRENCY_API_KEY', '106b30a68981c82ba4776b82f0fc6b69')
CURRENCY_API_ENDPOINT = os.getenv('CURRENCY_API_HOST', 'http://api.currencylayer.com/live')
