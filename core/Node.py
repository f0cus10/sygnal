#Node class 
#Xiangmin Mo and Sami Beig
class Node():

	#default constructor
	def __init__(self, x1, y1, ID, radius, CHANNELS):

		"""Initialize Node attributes"""
		self.x1 = x1
		self.y1 = y1
		self.ID = ID
		self.radius = radius
		self.UNUSED_CHANNELS_NODE = CHANNELS
		self.nodes = []
		self.USED_CHANNELS = []


