# import uuid
from flask import Blueprint, jsonify, request
# from db import database
# from grid_interface import generate_grid

import json 

main = Blueprint('main', __name__)

@main.route('/submitform', methods=['POST'])
def grid():
    form_data = request.get_json()
    print(form_data)
    #check if the args are valid first
    if 'numChannels' not in form_data.keys():
        return jsonify({ 'error': 'Insufficient arguments' }), 200
    
    # grid_id = uuid.uuid1()
    # storage_grid, res_grid = generate_grid()

    # database[grid_id] = storage_grid

    # return jsonify({'gridID': grid_id, 'grid': res_grid }), 201
    with open('./dummy/grid.json') as json_file:
        data = json.load(json_file)
        return jsonify(data)


@main.route('/getroute', methods=['GET'])
def getRoute():
    source_dest_data = request.get_json()
    print(source_dest_data)
    with open('./dummy/connections.json') as json_file:
        data = json.load(json_file)
        return jsonify(data)
