import os

import psycopg2

# Extract host and port from ngrok address
host, port = "127.0.0.1:5432".split(":")

# PostgreSQL connection parameters
dbname = os.environ.get('SQL_DB_NAME')
user = os.environ.get('SQL_USERNAME')
password = os.environ.get('SQL_PASSWORD')


def create_connection():
    return psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
