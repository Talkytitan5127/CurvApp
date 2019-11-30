from flask import (Blueprint, request, jsonify, make_response, current_app)
from flask import render_template

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/', methods=['GET'])
def index():
    return render_template('admin.html')
