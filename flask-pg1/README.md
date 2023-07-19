
Initial set-up:
```
sudo nala install libpq-dev
python3 -m venv env
. env/bin/activate
pip install flask
pip install pyscopg2
pip install python-dotenv
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
