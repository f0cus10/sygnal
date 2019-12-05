#Everything Class

from Node import Node
from baseStation import baseStation
import math
from collections import defaultdict 
import sys 
import random

# 2D array 
rows, cols = (100, 100) 
GRID = [[0 for i in range(cols)] for j in range(rows)] 
#print(arr)

#User inputted radius for nodes
NODE_RADIUS = 4

#User inputted radius for base stations
BASE_STATION_RADIUS = 10

#Randomly generated number of nodes, ranging from 1-10
numOfNodes = random.randrange(1, 10)

#Randomly generated number of Base Stations, ranging from 1 - 5
numOfBaseStations = random.randrange(1, 5)

#User input number of channels, ranging from 5 - 10
numOfChannels = 6

#Randomly plot nodes onto GRID
for node in range(numOfNodes):
	x = random.randrange(0,99)
	y = random.randrange(0,99)
	while GRID[x][y] != 0:
		x = random.randrange(0,99)
		y = random.randrange(0,99)
	GRID[x][y] = Node(x, y, node, NODE_RADIUS)


 #Randomly plot base stations onto GRID
for base in range(numOfBaseStations):
	x = random.randrange(0,99)
	y = random.randrange(0,99)
	while GRID[x][y] != 0:
		x = random.randrange(0,99)
		y = random.randrange(0,99)
	GRID[x][y] = baseStation(x, y, base, BASE_STATION_RADIUS)


print(GRID)



