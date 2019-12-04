from flask import Blueprint, jsonify, request

database = {}

main = Blueprint('main', __name__)

@main.route('/submitform', methods=['POST'])
def generate_grid():
    form_data = request.get_json()

    new_grid = ({ 'title': form_data['name'] })

    database['client-121'] = new_grid

    return 'Done', 201


@main.route('/getroute', methods=['GET'])
def getRoute():

    return jsonify(database)