Activate python environment (see below for environment set-up):
```
. env/bin/activate
```

Start the app/server running:
```
flask run
```

Initial set-up:
```
sudo nala install libpq-dev
python3 -m venv env
. env/bin/activate
pip install flask
pip install pyscopg  # DON'T use psycopg2!!
pip install python-dotenv
```

Create a database from songs.sql 
```
# First copy file into /var/lib/postgresql/prime
sudo cp songs.sql /var/lib/postgresql/prime/
su - postgres  # enter password
psql
CREATE DATABASE testdb
\c testdb
\i prime/songs.sql
```

Ceate a .env with postgres username and password
```
DB_USER=<username>
DB_PASSWORD=<password>
```

Create a .flaskenv with flask environment variables
```
FLASK_APP=app.py
FLASK_DEBUG=1
```
