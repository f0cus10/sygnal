#Everything Class

from Node import Node
from baseStation import baseStation
import math
from collections import defaultdict 
import sys 
import random
import numpy as np
from Grid import Grid

#Class to represent adj list of te node
class AdjNode:
  def __init__(self, data):
    self.vertex = data
    self.next = None

#class to represent graph
# size = number of vertices
class Graph:
  def __init__(self, vertices):
    self.V = vertices
    self.graph = [None] * self.V

  def addEdge(self,src,dest):
    # node = AdjNode(dest)
    # node.next = self.graph[src] 
    # self.graph[src] = node 
    # Adding the source node to the destination as 
    # it is the undirected graph 
    node = AdjNode(src) 
    node.next = self.graph[dest] 
    self.graph[dest] = node 

  def poopie(self):
    print("poopie")
 

  # Function to print the graph 
  def printGraph(self): 
    for i in range(self.V): 
      print("Adjacency list of vertex {}\n head".format(i), end="") 
      temp = self.graph[i] 
      while temp: 
        print(" -> {}".format(temp.vertex), end="") 
        temp = temp.next
      print(" \n")



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

#User inputted radius for nodes
NODE_RADIUS = 20

#User inputted radius for base stations
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

#Populates the dictionary with the key being the channel number, and the value being the associated probability
k = 0
while k < numOfChannels :
	LOGICAL_GRID.UNUSED_CHANNELS[k+1] = channelPoisson[k]
	k = k + 1

#Sorts the dictionary using the value (probability)
LOGICAL_GRID.UNUSED_CHANNELS = sorted(LOGICAL_GRID.UNUSED_CHANNELS.items(), key=lambda x: x[1])

i = 0
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

NODE_DICTIONARY = {}
for i in range(numOfNodes):
	NODE_DICTIONARY[i] = []

for m in LOGICAL_GRID.NODES:
	for n in LOGICAL_GRID.NODES:
		if m == n :
			#print("poopie")
			continue
		else :
			if LOGICAL_GRID.checkBaseStations(m, n) == 0 or LOGICAL_GRID.checkBaseStations(m, n) == 1:
				graph.addEdge(m.ID, n.ID)
				NODE_DICTIONARY[m.ID].append(n.ID)

print(NODE_DICTIONARY)


# for node in LOGICAL_GRID.NODES:
# 	print("NODE ID BELOW")
# 	print(node.ID)
# 	print(node.x1)
# 	print (node.y1)
# 	print(node.radius)

#BSNodes = {}
for base in LOGICAL_GRID.BASESTATIONS:
	for node in LOGICAL_GRID.NODES:
		if LOGICAL_GRID.addNodeToBaseStation(base, node) == True:
			# print(node)
			# print(base)
			#BSNodes[base].append(node)
			#print("ADDED")
			continue
		#else :
			#print('none')
			#print("NOT ADDED")
	
	#print(base.nodes)

#Shortest path from source to destination node being printed as a list
print(BFS(1, 2))
#print(BSNodes)


#LOGICAL_GRID.route(LOGICAL_GRID.NODES[0], LOGICAL_GRID.NODES[1])

#graph.printGraph()
#print("AFTER GRAPH IS PRINTED")
#graph.BFS(LOGICAL_GRID.NODES[0].ID, LOGICAL_GRID.NODES[1].ID)

