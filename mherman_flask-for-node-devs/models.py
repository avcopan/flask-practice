import sqlite3


def drop_table():
    with sqlite3.connect('songs.db') as connection:
        c = connection.cursor()
        c.execute("DROP TABLE IF EXISTS songs;")
    return True


def create_db():
    with sqlite3.connect('songs.db') as connection:
        c = connection.cursor()
        query_string = """
            CREATE TABLE songs(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              artist TEXT NOT NULL,
              title TEXT NOT NULL,
              rating INTEGER NOT NULL
            );
        """
        c.execute(query_string)
    return True


if __name__ == '__main__':
    drop_table()
    create_db()
