import Node

#Base Station class
class baseStation():

	#Initialize Base Station class

	#Constructor
	def __init__(self, x1, y1, ID, radius):
		self.x1 = x1
		self.y1 = y1
		self.ID = ID
		self.radius = radius
		self.nodes = []