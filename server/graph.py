#class to represent the graph
#vertices = number of vertices
class Graph:
  def __init__(self, vertices):
    self.V = vertices
    self.graph = [None] * self.V

#BFS algorithm
def BFS(start, goal, node_dict):
        explored = []
        queue = [[start]]

        if start == goal:
          return "Start = goal"

        while queue:

          path = queue.pop(0)
          node = path[-1]
          if node not in explored:
            neighbours = node_dict[node]
            for neighbor in neighbours:
              new_path = list(path)
              new_path.append(neighbor)
              queue.append(new_path)
              if neighbor == goal:
                return new_path
            explored.append(node)
        return "No path!"


