from flask import (Blueprint, request, jsonify, make_response, current_app)
from flask import render_template

from .db import Cursor

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/', methods=['GET'])
def index():
    cursor = Cursor()
    users = cursor.get_all_users()
    return render_template('admin.html', users=users)


@admin.route('/user/<int:db_id>', methods=['GET'])
def user(db_id):
    cursor = Cursor()
    
    user = cursor.get_user(None, db_id=db_id)
    timelist = cursor.get_user_time(user)
    
    cursor.close()

    return render_template(
        'user.html',
        user=user,
        timelist=timelist
    )
