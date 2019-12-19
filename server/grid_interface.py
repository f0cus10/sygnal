#grid_interface

import random
import numpy as np

from server.Grid import Grid
from server.Everything import Graph
from server.Node import Node
from server.baseStation import baseStation

def __nodePlotter(num_nodes, radius, channels, grid, shadow_grid):
	'''
	Randomly plots nodes onto grid and shadow_grid and then returns them
	'''
	id_counter = 0
	for node in range(num_nodes):
		x = random.randrange(0,99)
		y = random.randrange(0,99)
		while grid[x][y] is not 0:
			x = random.randrange(0,99)
			y = random.randrange(0,99)
		tmpNode = Node(x, y, id_counter, radius, channels[:])
		grid[x][y] = tmpNode
		shadow_grid.NODES.append(tmpNode)
		id_counter += 1
	return grid, shadow_grid

def __basePlotter(num_bases, radius, grid, shadow_grid):
	'''
	Randomly plots basestations onto the grid and shadow_grid and then returns
	'''
	base_counter = 0
	for base in range(num_bases):
		x = random.randrange(0,99)
		y = random.randrange(0,99)
		while grid[x][y] is not 0:
			x = random.randrange(0,99)
			y = random.randrange(0,99)
		tmpBs = baseStation(x, y, base_counter, radius)
		grid[x][y] = tmpBs
		shadow_grid.BASESTATIONS.append(tmpBs)

	return grid, shadow_grid

def generate_grid(num_channels):
	'''
	@params num_channels contain the # of channels available. 5 <= num_channels <= 10
	'''
	# 2D array 
	rows, cols = (100, 100) 
	resultant_grid_map = [[0 for i in range(cols)] for j in range(rows)]

	SHADOW_GRID = Grid()

	node_radius = 17
	base_station_radius = 15
	num_nodes = random.randrange(1,5)
	num_base_stations = random.randrange(1,5)
	
	print("Number of Nodes: " + str())
	print("Number of Base Stations: " + str())

	storage_graph = Graph(num_nodes)

	#Poisson point distro with lambda set to 80
	channelPoisson = np.random.poisson(lam=80, size=num_channels)

	#ensures values <1
	channelPoisson = channelPoisson/100

	channel_list = {}

	#maps channels with probability
	k = 0
	while k < num_channels:
		channel_list[k+1] = channelPoisson[k]
		k += 1
	
	#sorted according to quality
	channel_list = sorted(channel_list.items(), key=lambda x: x[1])

	print("List of channels (in order): ")
	print(channel_list)

	resultant_grid_map, SHADOW_GRID = __nodePlotter(num_nodes, node_radius, channel_list, resultant_grid_map, SHADOW_GRID)
	resultant_grid_map, SHADOW_GRID = __basePlotter(num_nodes, base_station_radius, resultant_grid_map, SHADOW_GRID)

	# Associations between nodes
	node_dict = {}
	for i in range(num_nodes):
		node_dict[i] = []
	
	for m in SHADOW_GRID:
		for n in SHADOW_GRID:
			if not m == n and SHADOW_GRID.checkTransmission(m, n) in [0,1]:
				node_dict[m.ID].append(n.ID)
				continue
	
	print("Node adjacency list: ")
	print(node_dict)

	# Associations with base stations
	for each_base in SHADOW_GRID.BASESTATIONS:
		for each_node in SHADOW_GRID.NODES:
			if SHADOW_GRID.addNodeToBaseStation(each_base, each_node):
				continue
	
	# TODO: Figure out the rest of the returning values
	return resultant_grid_map, SHADOW_GRID
	
	

