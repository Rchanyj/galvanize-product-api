import os

LISTEN_PORT = int(os.getenv('LISTEN_PORT', 8080))
PG_CONNECTION_STRING = os.getenv('PG_CONNECTION_STRING', 'dbname=DemoProducts host=postgres port=5432 user=postgres sslmode=disable')
