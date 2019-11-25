import json

from flask import Flask
from flaskext.mysql import MySQL

from . import db
from . import server


def config_db(app_instance):
    with open('../config/user_sql.json') as fh:
        data = json.load(fh)

    for key, value in data.items():
        app_instance.config[key] = value


app = Flask(__name__)
app.config.from_mapping(
    DEBUG=True,
)

app.mysql = MySQL()
app.mysql.init_app(app)

db.init_app(app)

app.register_blueprint(server.api)
