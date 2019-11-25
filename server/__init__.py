import os
import json

from flask import Flask
from flaskext.mysql import MySQL

from . import db
from . import server

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def config_db(app_instance):
    with open(f'{BASE_DIR}/config/user_sql.json') as fh:
        data = json.load(fh)

    for key, value in data.items():
        app_instance.config[key] = value


app = Flask(__name__)
app.config.from_mapping(
    DEBUG=True,
)
config_db(app)

app.mysql = MySQL()
app.mysql.init_app(app)

db.init_app(app)

app.register_blueprint(server.api)
