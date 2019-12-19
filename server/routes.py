import uuid

from flask import Blueprint, jsonify, request
import json

from db import database
from gridGeneration import generate_grid
from gridResolution import resolve

main = Blueprint('main', __name__)

@main.route('/submitform', methods=['POST'])
def grid():
    form_data = request.get_json()
    print(form_data)

    #check if the args are valid first
    if 'numChannels' not in form_data.keys():
        return jsonify({ 'error': 'Insufficient arguments' }), 200
    
    num_channels = int(form_data['numChannels'])

    if (num_channels < 5) or (num_channels > 10):
        return jsonify({'error': 'Channel number out of range'}), 200
    
    # generate new grid
    grid_id = uuid.uuid1()
    resolve_grid, storage_grid = generate_grid(num_channels)
    database[grid_id] = storage_grid
    # TODO: make the return based on JSONified graph
    return resolve(grid_id, resolve_grid), 201


@main.route('/getroute', methods=['GET'])
def getRoute():
    source_dest_data = request.get_json()
    print(source_dest_data)
    with open('./dummy/connections.json') as json_file:
        data = json.load(json_file)
        return jsonify(data)
