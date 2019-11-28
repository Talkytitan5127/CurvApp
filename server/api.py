from flask import (Blueprint, request, jsonify, make_response, current_app)

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/hello', methods=['GET'])
def hello():
    return jsonify(result='hello')


@api.route('/post_hello', methods=['POST'])
def post_hello():
    data = request.json
    current_app.logger.info('Server get data: {}'.format(data))

    return make_response(jsonify(data), 201)
