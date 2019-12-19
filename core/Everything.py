#Xiangmin Mo and Sami Beig
#------------------------------------------------------------------------------------------------------------------------------------------
#Everything Class
#The purpose of this class is to combine all of the classes created thus far (Node, Grid, and baseStation)
#This class uses numpy to calculate a poisson point distribution to determine channel arrival probability
#Plots Nodes and baseStation randomly on a 100x100 grid
#Nodes will gain neighbors based on transmission range
#Breadth-First Search is also implemented and modified to return the shortest path between two nodes (Unweighted graph is also constructed)
#------------------------------------------------------------------------------------------------------------------------------------------

from Node import Node
from baseStation import baseStation
import math
from collections import defaultdict 
import sys 
import random
import numpy as np
from Grid import Grid

#class to represent the graph
#vertices = number of vertices
class Graph:
  def __init__(self, vertices):
    self.V = vertices
    self.graph = [None] * self.V

#BFS algorithm
def BFS(start, goal):
	explored = []
	queue = [[start]]

	if start == goal:
	  return "Start = goal"

	while queue:

	  path = queue.pop(0)
	  node = path[-1]
	  if node not in explored:
	    neighbours = NODE_DICTIONARY[node]
	    for neighbor in neighbours:
	      new_path = list(path)
	      new_path.append(neighbor)
	      queue.append(new_path)
	      if neighbor == goal:
	        return new_path
	    explored.append(node)
	return "No path!"


# 2D array 
rows, cols = (100, 100) 
GRID = [[0 for i in range(cols)] for j in range(rows)] 
#print(arr)

#Grid class that will contain all the nodes and base stations via public methods
LOGICAL_GRID = Grid()

#Radius for nodes
NODE_RADIUS = 17

#Radius for base stations
BASE_STATION_RADIUS = 15

#Randomly generated number of nodes, ranging from 2-10
numOfNodes = random.randrange(2, 10)
print(numOfNodes)

graph = Graph(numOfNodes)

#Randomly generated number of Base Stations, ranging from 1 - 5
numOfBaseStations = random.randrange(1, 5)
print(numOfBaseStations)

#User input number of channels, ranging from 5 - 10
while True:
	numOfChannels = int(input("Enter the number of channels (from 5 to 10): "))
	if numOfChannels < 5 or numOfChannels > 10:
		print("Invalid number of channels.")
	else:
		break

#Poisson Point Distribution with lambda set to 80 for now
channelPoisson = np.random.poisson(lam=80, size=numOfChannels)

#Ensures that the value is less than 1
channelPoisson = channelPoisson/100


allChannels = {}

#Populates the dictionary with the key being the channel number, and the value being the associated probability
k = 0
while k < numOfChannels :
	allChannels[k+1] = channelPoisson[k]
	k = k + 1

#Sorts the dictionary using the value (probability)
allChannels = sorted(allChannels.items(), key=lambda x: x[1])

print("ALL CHANNELS BELOW")
print(allChannels)

i = 0
#Randomly plot nodes onto GRID
for node in range(numOfNodes):
	x = random.randrange(0,99)
	y = random.randrange(0,99)
	while GRID[x][y] != 0:
		x = random.randrange(0,99)
		y = random.randrange(0,99)
	tmpNode = Node(x, y, i, NODE_RADIUS, allChannels[:])
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

NODE_DICTIONARY = {}
for i in range(numOfNodes):
	NODE_DICTIONARY[i] = []

for m in LOGICAL_GRID.NODES:
	for n in LOGICAL_GRID.NODES:
		if m == n :
			#print("poopie")
			continue
		else :
			if LOGICAL_GRID.checkTransmission(m, n) == 0 or LOGICAL_GRID.checkTransmission(m, n) == 1:
				NODE_DICTIONARY[m.ID].append(n.ID)

print(NODE_DICTIONARY)

for base in LOGICAL_GRID.BASESTATIONS:
	for node in LOGICAL_GRID.NODES:
		if LOGICAL_GRID.addNodeToBaseStation(base, node) == True:
			continue

ALL_PATHS = []

while True:
	#Shortest path from source to destination node being printed as a list
	VERIFICATION = input("Want to continue? Enter \'continue\' or \'quit\': \n")
	if VERIFICATION == 'continue':
		
		#ensures user inputs positive number
		source = int(input("Enter Source: "))
		if source < 0:
			print("Enter positive number.")
			continue

		#ensures user inputs positive number
		destination = int(input("Enter Destination: "))
		if destination < 0:
			print("Enter positive number.")
			continue

		path = BFS(source, destination)
		
		if path == "No path!":
			continue

		reverse_path = path[:]

		print("Shortest Path: " + str(path))
		length = len(BFS(source,destination))
		channelsToRemove = allChannels[:length-1]
		
		#Add the path and the reverse path to prevent user input same path
		if path in ALL_PATHS:
			print("Path already exists")
			continue
		else:
			ALL_PATHS.append(path)
			reverse_path.reverse()
			ALL_PATHS.append(reverse_path)


		print("BEFORE: ")
		for i in range(len(LOGICAL_GRID.NODES)):
			print("<" + str(LOGICAL_GRID.NODES[i].ID) + ">: " + str(LOGICAL_GRID.NODES[i].UNUSED_CHANNELS_NODE))

		for i in range(len(path)):
			k = path[i]
			if i != len(path)-1:
				#for j in range(len(channelsToRemove)):
				nextNode = LOGICAL_GRID.NODES[path[i+1]]
				startOfUnusedChannel = LOGICAL_GRID.NODES[k].UNUSED_CHANNELS_NODE[0]

				if (startOfUnusedChannel not in LOGICAL_GRID.NODES[k].USED_CHANNELS) and (startOfUnusedChannel not in nextNode.USED_CHANNELS):
					
					LOGICAL_GRID.NODES[k].USED_CHANNELS.append(startOfUnusedChannel)
					LOGICAL_GRID.NODES[path[i+1]].USED_CHANNELS.append(startOfUnusedChannel)
					LOGICAL_GRID.NODES[k].UNUSED_CHANNELS_NODE.remove(startOfUnusedChannel)
					LOGICAL_GRID.NODES[path[i+1]].UNUSED_CHANNELS_NODE.remove(startOfUnusedChannel)

				elif (startOfUnusedChannel in LOGICAL_GRID.NODES[k].USED_CHANNELS):

					for p in range(len(LOGICAL_GRID.NODES[k].UNUSED_CHANNELS_NODE)):

						if (LOGICAL_GRID.NODES[k].UNUSED_CHANNELS_NODE[p] + 1 in LOGICAL_GRID.NODES[k].USED_CHANNELS) or (LOGICAL_GRID.NODES[k].UNUSED_CHANNELS_NODE[p] - 1 in LOGICAL_GRID.NODES[k].USED_CHANNELS):
							continue
						else:

							LOGICAL_GRID.NODES[k].USED_CHANNELS.append(startOfUnusedChannel)
							LOGICAL_GRID.NODES[path[i+1]].USED_CHANNELS.append(startOfUnusedChannel)
							LOGICAL_GRID.NODES[k].UNUSED_CHANNELS_NODE.remove(startOfUnusedChannel)
							LOGICAL_GRID.NODES[path[i+1]].UNUSED_CHANNELS_NODE.remove(startOfUnusedChannel)

							break
					
			else:
				break

		
		#Debug
		print("AFTER: ")
		for i in range(len(LOGICAL_GRID.NODES)):
			print("<" + str(LOGICAL_GRID.NODES[i].ID) + ">: " + str(LOGICAL_GRID.NODES[i].UNUSED_CHANNELS_NODE))

	elif VERIFICATION == 'quit':
		break

	else:
		print("Invalid input!")
		continue