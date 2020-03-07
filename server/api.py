from flask import (Blueprint, request, jsonify, make_response, current_app)
from .db import Cursor
from flask import current_app
from datetime import datetime
import sys

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/hello', methods=['GET'])
def hello():
    return jsonify(result='hello')


@api.route('/post_hello', methods=['POST'])
def post_hello():
    data = request.json
    current_app.logger.info('Server get data: {}'.format(data))

    return make_response(jsonify(data), 201)


@api.route('/user', methods=['POST'])
def create_user():
    data = request.json
    cursor = Cursor()
    user = cursor.create_user(data)
    user_uuid = user.uuid
    cursor.commit([user])
    
    return make_response({"status": "created", "uuid": user_uuid}, 201)


@api.route('/user/<string:u_id>', methods=['GET'])
def get_user(u_id):
    cursor = Cursor()
    user = cursor.get_user(u_id)

    if user is None:
        return make_response(jsonify({'error': 'not found'}), 404)

    #work time
    is_exit = False
    timelist = cursor.get_user_time(user)
    if len(timelist) % 2:
        is_exit = True

    record = cursor.create_time(user, is_exit)
    cursor.commit([record])

    return make_response(jsonify({
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_exit': is_exit,
    }), 200)


@api.route('/user/<int:primary_id>', methods=['GET'])
def get_user_by_id(primary_id):
    data = {
        'date': request.args.get('date'),
        'time': request.args.get('time')
    }
    datetime_obj = datetime.strptime("{} {}".format(data['date'], data['time']), '%d-%m-%y %H:%M:%S')
    current_app.logger.info('DATA', data)
    print(data, file=sys.stderr)
    cursor = Cursor()
    user = cursor.get_user(None, db_id=primary_id)

    if user is None:
        return make_response(jsonify({'error': 'not found'}), 404)

    #work time
    is_exit = False
    timelist = cursor.get_user_time(user)
    if len(timelist) % 2:
        is_exit = True

    record = cursor.create_time(user, is_exit, datetime_obj)
    cursor.commit([record])

    return make_response(jsonify({
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_exit': is_exit,
        'time': data['time'],
    }), 200)

@api.route('/user/<int:user_id>/statistic', methods=['GET'])
def get_statistic(user_id):
    cursor = Cursor()
    user = cursor.get_user(db_id=user_id)

    if user is None:
        return make_response((jsonify({'statistic': None})))

