from flask import (Blueprint, request, jsonify, make_response, current_app)

from .db import Cursor

api = Blueprint('server', __name__, url_prefix='/api')


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
    cursor.close()
    return make_response({"status": "created", "uuid": user_uuid}, 201)


@api.route('/user/<string:u_id>', methods=['GET'])
def get_user(u_id):
    cursor = Cursor()
    user = cursor.get_user(u_id)
    cursor.close()
    if user is None:
        return make_response(jsonify({'error': 'not found'}), 404)

    return make_response(jsonify({
        'first_name': user.first_name,
        'last_name': user.last_name
    }), 200)
