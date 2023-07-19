import json
import sqlite3
import flask

app = flask.Flask(__name__)


@app.route('/api/songs', methods=['GET', 'POST'])
def collection():
    if flask.request.method == 'GET':
        songs = get_songs()
        return json.dumps(songs)
    elif flask.request.method == 'POST':
        data = flask.request.form
        result = add_song(data['artist'], data['title'], data['rating'])
        return flask.jsonify(result)


@app.route('/api/song/<song_id>', methods=['GET', 'PUT', 'DELETE'])
def resource(song_id):
    if flask.request.method == 'GET':
        song = get_song(song_id)
        return json.dumps(song)
    elif flask.request.method == 'PUT':
        data = flask.request.form
        result = edit_song(
            song_id, data['artist'], data['title'], data['rating'])
        return flask.jsonify(result)
    elif flask.request.method == 'DELETE':
        result = delete_song(song_id)
        return flask.jsonify(result)


# helper functions
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


def get_songs():
    with sqlite3.connect('songs.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM songs ORDER BY id DESC;")
        songs = cursor.fetchall()
        return songs


def get_song(song_id):
    with sqlite3.connect('songs.db') as connection:
        cursor = connection.cursor()
        query_string = "SELECT * FROM songs WHERE id = ?;"
        query_params = (song_id,)
        print('query_params', query_params)
        cursor.execute(query_string, query_params)
        song = cursor.fetchone()
        print('song', song)
        return song


def edit_song(song_id, artist, title, rating):
    try:
        with sqlite3.connect('songs.db') as connection:
            cursor = connection.cursor()
            query_string = """
                UPDATE songs SET artist = ?, title = ?, rating = ?
                WHERE id = ?;"""
            query_params = (artist, title, rating, song_id,)
            cursor.execute(query_string, query_params)
            result = {'status': 1, 'message': 'Song edited'}
    except:
        result = {'status': 0, 'message': 'Error'}
    return result


def delete_song(song_id):
    try:
        with sqlite3.connect('songs.db') as connection:
            cursor = connection.cursor()
            query_string = "DELETE FROM songs WHERE id = ?;"
            query_params = (song_id,)
            cursor.execute(query_string, query_params)
            result = {'status': 1, 'message': 'Song deleted'}
    except:
        result = {'status': 0, 'message': 'Error'}
    return result
