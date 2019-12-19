#class to represent the graph
#vertices = number of vertices
class Graph:
  def __init__(self, vertices):
    self.V = vertices
    self.graph = [None] * self.V
