Activate python environment:
```
. env/bin/activate
```

Start the app/server (make sure FLASK_APP and FLASK_DEBUG are set -- see below):
```
flask run
```

Start sqlite session:
```
sqlite3 songs.db
```

Initial set up:
```
sudo nala install sqlite3
python3 -m venv env
. env/bin/activate
pip install flask
pip freeze > requirements.txt
```

NOTE I also added the following lines to env/bin/activate:
```
export FLASK_APP=app.py;
export FLASK_DEBUG=1;
```