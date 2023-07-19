import json
import flask
import utils

CONN = utils.pg.connection()

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
        with CONN.cursor() as cursor:
            query_params = [artist, title, rating]
            query_string = """
                INSERT INTO songs (artist, title, rating) values (%s, %s, %s);"""
            cursor.execute(query_string, query_params)
            print("Executed")
            result = {'status': 1, 'message': 'Song added'}
    except Exception as error:
        result = {'status': 0, 'message': f'Error: {error}'}
    return result


def get_songs():
    with CONN.cursor() as cursor:
        cursor.execute("SELECT * FROM songs;")
        songs = cursor.fetchall()
        print("Sending songs:", songs)
        return songs


def get_song(song_id):
    with CONN.cursor() as cursor:
        query_string = "SELECT * FROM songs WHERE id = %s;"
        query_params = [song_id]
        print('query_params', query_params)
        cursor.execute(query_string, query_params)
        song = cursor.fetchone()
        print('song', song)
        return song


def edit_song(song_id, artist, title, rating):
    try:
        with CONN.cursor() as cursor:
            query_string = """
                UPDATE songs SET artist = %s, title = %s, rating = %s
                WHERE id = %s;"""
            query_params = [artist, title, rating, song_id]
            cursor.execute(query_string, query_params)
            result = {'status': 1, 'message': 'Song edited'}
    except Exception as error:
        result = {'status': 0, 'message': f'Error: {error}'}
    return result


def delete_song(song_id):
    try:
        with CONN.cursor() as cursor:
            query_string = "DELETE FROM songs WHERE id = %s;"
            query_params = [song_id]
            cursor.execute(query_string, query_params)
            result = {'status': 1, 'message': 'Song deleted'}
    except Exception as error:
        result = {'status': 0, 'message': f'Error: {error}'}
    return result
