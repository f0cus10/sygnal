import uuid
from flask import Blueprint, jsonify, request
from db import database
from grid_interface import generate_grid

main = Blueprint('main', __name__)

@main.route('/submitform', methods=['POST'])
def grid():
    form_data = request.get_json()

    #check if the args are valid first
    if 'numChannels' not in form_data.keys():
        return jsonify({ 'error': 'Insufficient arguments' }), 200
    
    storage_grid, res_grid = generate_grid()


    return jsonify({'gridID': 1, 'grid': res_grid }), 201


@main.route('/getroute', methods=['GET'])
def getRoute():

    return jsonify(database)