import os
import dotenv
import psycopg

dotenv.load_dotenv()

def connection():
  conn = psycopg.connect(
      dbname="testdb",
      user=os.getenv('DB_USER'),
      password=os.getenv('DB_PASSWORD'),
      host="localhost",
      port="5432",
  )
  return conn
