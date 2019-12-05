#grid_interface

import math
from collections import defaultdict 
import sys 
import random
from Node import Node
from baseStation import baseStation

# #User input number of channels, ranging from 5 - 10
# numOfChannels = 6

def generate_grid():
	'''
	@params param_dict contains the relevant parameters necessary to generate the grid
	'''
	#randomly generate the variables
	node_radius = 4
	base_station_radius = 10
	num_nodes = random.randrange(1, 10)
	num_stations = random.randrange(1,5)

	#generate a zero 2D array
	rows, cols = (100, 100)
	GRID = [[0 for i in range(cols)] for j in range(rows)]
	shadow_map = [['Z' for i in range(cols)] for j in range(rows)]

	#Randomly plot nodes onto GRID
	for node in range(num_nodes):
		x = random.randrange(0,99)
		y = random.randrange(0,99)
		while GRID[x][y] != 0:
			x = random.randrange(0,99)
			y = random.randrange(0,99)
		GRID[x][y] = Node(x, y, node, node_radius)
		shadow_map[x][y] = 'N' + str(node)
	
	#Randomly plot base stations onto GRID
	for base in range(num_stations):
		x = random.randrange(0,99)
		y = random.randrange(0,99)
		while GRID[x][y] != 0:
			x = random.randrange(0,99)
			y = random.randrange(0,99)
		GRID[x][y] = baseStation(x, y, base, base_station_radius)
		shadow_map[x][y] = 'B' + str(node)
		

	return GRID, shadow_map