#Everything Class

import math
from collections import defaultdict 
import sys 
import random
from Node import Node
from baseStation import baseStation

# #User input number of channels, ranging from 5 - 10
# numOfChannels = 6

def generate_grid(param_dict):
	'''
	@params param_dict contains the relevant parameters necessary to generate the grid
	'''
	#generate a zero 2D array
	rows, cols = (100, 100)
	GRID = [[0 for i in range(cols)] for j in range(rows)]
	shadow_map = [['Z' for i in range(cols)] for j in range(rows)]

	#Randomly plot nodes onto GRID
	for node in range(param_dict['num_nodes']):
		x = random.randrange(0,99)
		y = random.randrange(0,99)
		while GRID[x][y] != 0:
			x = random.randrange(0,99)
			y = random.randrange(0,99)
		GRID[x][y] = Node(x, y, node, param_dict['NODE_RADIUS'])
		shadow_map[x][y] = 'N' + str(node)
	
	#Randomly plot base stations onto GRID
	for base in range(param_dict['num_stations']):
		x = random.randrange(0,99)
		y = random.randrange(0,99)
		while GRID[x][y] != 0:
			x = random.randrange(0,99)
			y = random.randrange(0,99)
		GRID[x][y] = baseStation(x, y, base, param_dict['BASE_STATION_RADIUS'])
		shadow_map[x][y] = 'B' + str(node)
		

	return GRID, shadow_map