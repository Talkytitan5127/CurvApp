import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    db = getattr(g, '_db', None)
    if db is None:
        db = g._db = current_app.mysql.connect()

    return db


def close_db(e=None):
    db = getattr(g, '_db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()
    print("Process init_db")


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
