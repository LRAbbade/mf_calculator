import psycopg2
import os


host = os.environ['DB_HOST']
port = os.environ['DB_PORT']
db_name = os.environ['POSTGRES_DB']
user = os.environ['DB_USER']
pwd = os.environ['POSTGRES_PASSWORD']

conn = psycopg2.connect(host=host, port=port, database=db_name, user=user, password=pwd)
cur = conn.cursor()
