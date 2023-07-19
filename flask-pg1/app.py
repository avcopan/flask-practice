import os
import dotenv
import psycopg2 as ppg

dotenv.load_dotenv()

conn = ppg.connect(
    dbname="testdb",
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host="localhost",
    port="5432",
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM test1;")
print(cursor.fetchall())