import urllib3
import json

BROKER_URL = 'Enter broker URL here'

http = urllib3.PoolManager()

def publish_msg(msg, topicId):
  encoded_msg = json.dumps(msg).encode('utf-8')

  r = http.request(
    'POST', 
    BROKER_URL+ '/' + str(topicId),
    body=encoded_msg,
    headers={'Content-Type': 'application/json'}
  )


def encode_node(node):
  result = {
    'x-coordinate': node.x1,
    'y-coordinate': node.y1,
    'nodeId': node.ID,
    'radius': node.radius,
    'unused-channels': node.UNUSED_CHANNEL_NODE,
    'connected-nodes': node.nodes,
    'used-channels': node.USED_CHANNELS
  }

  return result

def encode_station(base):
  result = {
    'x-coordinate': base.x1,
    'y-coordinate': base.y1,
    'baseId': base.ID,
    'radius': base.radius,
    'connected-nodes': base.nodes
  }

  return result


def transmit_logical_grid(grid, topicId, grid_dims=(100,100)):
  
  grid_dict = {
    'grid-rows': grid_dims[0],
    'grid-cols': grid_dims[1],
    'numNodes': len(grid.NODES),
    'nodes': [encode_node(node) for node in grid.NODES],
    'numStations': len(grid.BASESTATIONS),
    'stations': [encode_station(station) for station in grid.BASESTATIONS]
  }

  publish_msg(grid_dict, topicId)

