import os
import json

import click
from flask import Flask
from flask.cli import with_appcontext
from sqlalchemy import create_engine

from . import api
from . import admin

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
app.config.from_mapping(
    DEBUG=True,
)


def config_db(app_instance):
    with open(f'{BASE_DIR}/config/user_sql.json') as fh:
        data = json.load(fh)

    for key, value in data.items():
        app_instance.config[key] = value


config_db(app)

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)

app.register_blueprint(api.api)
app.register_blueprint(admin.admin)


def init_db():
    from .models import Base
    Base.metadata.create_all(engine)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


app.cli.add_command(init_db_command)
