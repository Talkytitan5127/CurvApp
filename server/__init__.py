import os
import json

import click
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

from . import server

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def config_db(app_instance):
    with open(f'{BASE_DIR}/config/user_sql.json') as fh:
        data = json.load(fh)

    for key, value in data.items():
        app_instance.config[key] = value


def init_db(app_instance):
    config_db(app_instance)
    db = SQLAlchemy(app_instance)
    db.create_all()


app = Flask(__name__)
app.config.from_mapping(
    DEBUG=True,
)
config_db(app)

app.mysql = SQLAlchemy(app)

app.register_blueprint(server.api)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db(app)
    click.echo('Initialized the database.')


app.cli.add_command(init_db_command)
