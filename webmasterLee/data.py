import sqlite3

import click
from flask import current_app, g

# https://flask.palletsprojects.com/en/3.0.x/tutorial/database/

# to create database, use terminal command
#     >>$ flask --app webmasterLee init-db


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schemalite.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)



# postgres 

# import psycopg2


## need to put username & password in the os env
## os.environ["DB_USERNAME"]
## os.environ["DB_PASS"]
# conn = psycopg2.connect(
#     host="localhost",
#     database="lee_development",
#     user="lemur",
#     password="~=KujC%.`xr*$jo;TkQM",
# )

# cur = conn.cursor()

# exectute command from file 
# with open("schema.sql", 'r') as f:
#     cur.execute(f.read())