#Everything Class

from Node import Node
from baseStation import baseStation
import math
from collections import defaultdict 
import sys 
import random
from Grid import Grid

# 2D array 
rows, cols = (100, 100) 
GRID = [[0 for i in range(cols)] for j in range(rows)] 
#print(arr)

#Grid class that will contain all the nodes and base stations via public methods
LOGICAL_GRID = Grid()

#User inputted radius for nodes
NODE_RADIUS = 20

#User inputted radius for base stations
BASE_STATION_RADIUS = 30

#Randomly generated number of nodes, ranging from 1-10
numOfNodes = random.randrange(1, 10)

#Randomly generated number of Base Stations, ranging from 1 - 5
numOfBaseStations = random.randrange(1, 5)

#User input number of channels, ranging from 5 - 10
numOfChannels = 6

i = 1
#Randomly plot nodes onto GRID
for node in range(numOfNodes):
	x = random.randrange(0,99)
	y = random.randrange(0,99)
	while GRID[x][y] != 0:
		x = random.randrange(0,99)
		y = random.randrange(0,99)
	tmpNode = Node(x, y, i, NODE_RADIUS)
	GRID[x][y] = tmpNode
	LOGICAL_GRID.NODES.append(tmpNode)
	i+=1


j = 1
#Randomly plot base stations onto GRID
for base in range(numOfBaseStations):
	x = random.randrange(0,99)
	y = random.randrange(0,99)
	while GRID[x][y] != 0:
		x = random.randrange(0,99)
		y = random.randrange(0,99)
	tmpBS = baseStation(x, y, j, BASE_STATION_RADIUS)
	GRID[x][y] = tmpBS
	LOGICAL_GRID.BASESTATIONS.append(tmpBS)
	j+=1

#Updates n1's neighbors based on transmission range and coordinates
def getNeighbors(n1):
	for node in LOGICAL_GRID.NODES:
		#don't want to compare n1 in NODES to itself
		if n1 != node:
			#if node is within range, add to nodes list of neighbors
			if LOGICAL_GRID.distanceFormula(n1, node) <= n1.radius:
				n1.NodesInRange.append(node)


#After accessing all the nodes and base stations, we need to update the neighbors for each node
for node in LOGICAL_GRID.NODES:
	getNeighbors(node)

k = 0
for node in LOGICAL_GRID.NODES:
	print(LOGICAL_GRID.NODES[k].NodesInRange)
	k+=1


LOGICAL_GRID.dijkstra(LOGICAL_GRID.NODES[0], LOGICAL_GRID.NODES[1])


