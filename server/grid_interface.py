#grid_interface

import math
from collections import defaultdict 
import sys 
import random
from Node import Node
from baseStation import baseStation

# #User input number of channels, ranging from 5 - 10
# numOfChannels = 6

def generate_grid(num_channels):
	'''
	@params param_dict contains the relevant parameters necessary to generate the grid
	'''
	# 2D array 
	rows, cols = (100, 100) 
	GRID = [[0 for i in range(cols)] for j in range(rows)]
	
	

