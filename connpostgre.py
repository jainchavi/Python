import psycopg2
import pandas as pd
from sqlalchemy import create_engine


conn = psycopg2.connect(
    dbname='postgres',
    user = 'postgres',
    password = 'chavijain@0209',
    host = 'localhost',
    port = '5432'

)

conn.autocommit = True

cur = conn.cursor()

cur.execute("DROP DATABASE IF EXISTS DB2;")
cur.execute("CREATE DATABASE DB2;")


