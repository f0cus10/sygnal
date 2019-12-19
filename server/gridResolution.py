from Node import Node
from baseStation import baseStation
from flask import jsonify

def resolve(grid_id, grid):
    json_grid = []
    for i in range(99):
        for j in range(99):
            if type(grid[i][j]) == type(baseStation(0,0,0,0)):
                # we have a base station
                bs_dict = {
                    "type": "BaseStation",
                    "name": "bs" + str(grid[i][j].ID),
                    "id": grid[i][j].ID,
                    "x": i,
                    "y": j,
                    "customComponent": "circle",
                    "size": grid[i][j].radius,
                    "style": {
                        "fill": "orange"
                    }
                }
                json_grid.append(bs_dict)
            elif type(grid[i][j]) == type(Node(0,0,0,0,[])):
                # we have a node
                node_dict = {
                    "type": "Node",
                    "name": "node" + str(grid[i][j].ID),
                    "id": grid[i][j].ID,
                    "x": i,
                    "y": j,
                    "customComponent": "square",
                    "size": grid[i][j].radius,
                }
                json_grid.append(node_dict)
            elif type(grid[i][j] == type(0)):
                continue
            else:
                return jsonify({"error": "Unknown object detected"})

    return jsonify(grid=json_grid, grid_id=grid_id)        
    pass