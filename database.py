import psycopg2 # type: ignore

CREATE_POLLS = """CREATE TABLE IF NOT EXISTS polls (id SERIAL PRIMARY KEY, title TEXT, owner TEXT);
"""
CREATE_OPTIONS = """CREATE TABLE IF NOT EXISTS options
(id SERIAL PRIMARY KEY, option_text TEXT, poll_id INTEGER);
"""
CREATE_VOTES = """CREATE TABLE IF NOT EXISTS votes (username TEXT, option_id INTEGER);
"""

NEW_POLL = """INSERT INTO polls (title, owner) VALUES (%s, %s)
"""

GET_ALL_POLLS = """SELECT * FROM polls;
"""

db_uri = "postgres://postgres:12345@localhost:5432/PollApp"
conn = psycopg2.connect(db_uri)

with conn:
    with conn.cursor() as cur:
        cur.execute(CREATE_POLLS)
        cur.execute(CREATE_OPTIONS)
        cur.execute(CREATE_VOTES)

def new_poll(title, owner):
    with conn:
        with conn.cursor() as cur:
            cur.execute(NEW_POLL, (title, owner))

def get_polls():
    with conn.cursor() as cur:
        cur.execute(GET_ALL_POLLS)
        return cur.fetchall()