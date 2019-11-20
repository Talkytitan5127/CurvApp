import os

from flask import Flask

app = Flask(__name__)
app.config.from_mapping(
    DEBUG=True,
)

from . import server
app.register_blueprint(server.api)
