import json
import sqlite3
import flask

app = flask.Flask(__name__)


@app.route('/api/songs', methods=['GET', 'POST'])
def collection():
    if flask.request.method == 'GET':
        all_songs = get_all_songs()
        return json.dumps(all_songs)
    elif flask.request.method == 'POST':
        data = flask.request.form
        result = add_song(data['artist'], data['title'], data['rating'])
        return flask.jsonify(result)


@app.route('/api/song/<song_id>', methods=['GET', 'PUT', 'DELETE'])
def resource(song_id):
    if flask.request.method == 'GET':
        pass
    elif flask.request.method == 'PUT':
        pass
    elif flask.request.method == 'DELETE':
        pass


# helper functions
def get_all_songs():
    with sqlite3.connect('songs.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM songs ORDER BY id DESC;")
        all_songs = cursor.fetchall()
        return all_songs


def add_song(artist, title, rating):
    try:
        with sqlite3.connect('songs.db') as connection:
            cursor = connection.cursor()
            query_params = (artist, title, rating)
            query_string = """
                INSERT INTO songs (artist, title, rating) values (?, ?, ?);"""
            cursor.execute(query_string, query_params)
            result = {'status': 1, 'message': 'Song added'}
    except:
        result = {'status': 0, 'message': 'Error'}
    return result
