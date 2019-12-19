#Grid Class
#Xiangmin Mo and Sami Beig
#Constructs a grid class that contains all of the baseStations and Nodes in a single list
#Algorithm for checking transmission range is included in this file
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
		# self.USED_CHANNELS = {}
		# self.UNUSED_CHANNELS = {}
		#self.DISTANCES = {}

	#Add nodes to a base station
	def addNodeToBaseStation(self, b1 , n1):
		#Checking if n1 is within transmission range of b1
		if self.nodeInBaseStation(b1, n1) == True :	
			b1.nodes.append(n1)
			return True
		else :
			return False


	"""There are three conditions that arise.
		1. If C1C2 == R1 + R2
     		Circles A and B are touching each other.
		2. If C1C2 > R1 + R2
     		Circles A and B are not touching each other.
     	3. If C1C2 < R1 + R2
      		Circles intersect each other. """
    
	#Checks whether b1 and b2 intersect using their transmission range
	def checkTransmission(self, b1, b2):
		x = (b2.x1 - b1.x1)**2
		y = (b2.y1 - b1.y1)**2
		dist = (x + y)
		radSumSq = (b1.radius + b2.radius) ** 2
		if (dist == radSumSq):
				return 1 
		elif (dist > radSumSq):
				return -1 
		else:
				return 0 

	#Check if n1 is in b1's transmission range
	def nodeInBaseStation(self, b1, n1):
		x = (n1.x1 - b1.x1)**2
		y = (n1.y1 - b1.y1)**2

		newRadius = b1.radius**2

		if ((x + y) < newRadius):
			return True
		else:
			return False

