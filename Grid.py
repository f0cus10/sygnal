#Grid Class

import Node
import baseStation
import math
from collections import defaultdict 
import sys 

def Grid():


	#constructor
	def __init__(self):
		self.BASESTATIONS = []
		self.NODES = []
		self.USED_CHANNELS = []
		self.UNUSED_CHANNELS = []

	#returns true if n1 is in b1's transmission range
	def checkTransmission(b1, n1):
		if ((b1.x1 + b1.radius) < (n1.x1) && (b1.y1 + b1.radius) < (n1.y1)) || ((b1.x1 - b1.radius) > (n1.x1) && (b1.y1 - b1.radius) > (n1.y1))
			return true

		return false


	#Add nodes to a base station
	def addNodeToBaseStation(b1 , n1):
		#Checking if n1 is within transmission range of b1
		if checkTransmission(b1, n1):
			b1.addNodes(n1)


	#distance formula, taking in two nodes
	def distanceFormula(n1, n2):
		x = (n2.x1 - n1.x1)**2
		y = (n2.y1 - n1.y1)**2

		ans = math.sqrt(x + y)

		return ans

	#finding neighbors
	def getNeighboring(n1):




