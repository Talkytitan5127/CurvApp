from flask import (Blueprint, request, jsonify, make_response, current_app)
from flask import render_template

from .db import Cursor

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/', methods=['GET'])
def index():
    cursor = Cursor()
    users = cursor.get_all_users()
    return render_template('admin.html', users=users)
