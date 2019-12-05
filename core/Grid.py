#Grid Class

import Node
import baseStation
import math
from collections import defaultdict 
import sys 

class Grid():


	#constructor
	def __init__(self):
		self.BASESTATIONS = []
		self.NODES = []
		self.USED_CHANNELS = []
		self.UNUSED_CHANNELS = []
		self.DISTANCES = {}
		self.DIJKSTRAS = {}

	#returns true if n1 is in b1's transmission range
	def checkTransmission(self, b1, n1):
		if ((b1.x1 + b1.radius) < (n1.x1) and (b1.y1 + b1.radius) < (n1.y1)) or ((b1.x1 - b1.radius) > (n1.x1) and (b1.y1 - b1.radius) > (n1.y1)):
			return True

		return False


	#Add nodes to a base station
	def addNodeToBaseStation(self, b1 , n1):
		#Checking if n1 is within transmission range of b1
		if checkTransmission(b1, n1):
			b1.addNodes(n1)
			return True
			


	#distance formula, taking in two nodes, can be applicable for nodes and base stations
	def distanceFormula(self, n1, n2):
		x = (n2.x1 - n1.x1)**2
		y = (n2.y1 - n1.y1)**2

		ans = math.sqrt(x + y)

		return ans

	"""There are three conditions that arise.
		1. If C1C2 == R1 + R2
     		Circles A and B are touching each other.
		2. If C1C2 > R1 + R2
     		Circles A and B are not touching each other.
     	3. If C1C2 < R1 + R2
      		Circles intersect each other. """
    #Checks whether b1 and b2 intersect using their transmission range
    #Can be applicable to nodes or base stations
	def checkBaseStations(self, b1, b2): 
	    dist = distanceFormula(b1, b2) 
	    radSumSq = (b1.radius + b2.radius) * (b1.radius + b2.radius);  
	    if (dist == radSumSq): 
	        return 1 
	    elif (dist > radSumSq): 
	        return -1 
	    else: 
	        return 0 


	#Dijkstra's Algorithm
	#n1 - source
	#n2 - destination
	def dijkstra(self, n1, n2):

		#Checking if n1 is in base station range, stores the base station in b1
		"""
		for base in BASESTATIONS:
			if addNodeToBaseStation(base, n1) == True:
				b1 = baseStation(base.x1, base.y1, base.ID, base.radius)
				break

		
		#Checking if n2 is in base station range, stores the base station in b2
		for base in BASESTATIONS:
			if addNodeToBaseStation(base, n2) == True:
				b2 = baseStation(base.x1, base.y1, base.ID, base.radius)
				break

		"""

		#if this is true, we do not need to call checkBaseStations function
		#if b1 == b2:


		#Dijstra code

		#DISTANCES - distance from one node to every other node stored in a dictionary
		"""
		distances = {
		    'B': {'A': 5, 'D': 1, 'G': 2},
		    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
		    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
		    'G': {'B': 2, 'D': 1, 'C': 2},
		    'C': {'G': 2, 'E': 1, 'F': 16},
		    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
		    'F': {'A': 5, 'E': 2, 'C': 16}}
		"""
		#looping through NODES to populate DISTANCES appropriately 
		#Assume that getNeighbors has already been called in Everything class
		for node in self.NODES:
			#If the node has neighbors within its transmission range, update DISTANCES
			if len(node.NodesInRange) != 0:
				#loop through the nodes in currentNode's list of neighbors
				for neighbor in node.NodesInRange:
					self.DISTANCES[node] = {}
					self.DISTANCES[node][neighbor] = self.distanceFormula(node, neighbor)

		#If there are no nodes in range of the source node
		if len(self.DISTANCES) == 0:
			print("No nodes in range")
		
		#If there ARE nodes within range of the source node
		else:
			print(self.DISTANCES)
			print("Hi")

			#NODES - list of all nodes in grid
			#dictionary that is updated periodically with shortest distances from each node
			unvisited = {node: None for node in self.NODES} #using None as +inf

			#dictionary that stores which nodes are visited already
			visited = {}

			#current =  user decides to be the start node through Everything class
			current = n1

			#destinationNode = n2 (User inputted through Everything class)
			destinationNode = n2
			currentDistance = 0
			unvisited[current] = currentDistance

			#Dijkstra's algorithm
			while True:
			    for neighbour, distance in self.DISTANCES[current].items():
			        if neighbour not in unvisited: continue
			        newDistance = currentDistance + distance
			        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
			            unvisited[neighbour] = newDistance
			    visited[current] = currentDistance
			    del unvisited[current]
			    if not unvisited: break
			    candidates = [node for node in unvisited.items() if node[1]]
			    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

			#If destinationNode is not in visited, there is no route available
			if destinationNode not in visited:
				print("No route found!")
			else:
				print("Route established")



