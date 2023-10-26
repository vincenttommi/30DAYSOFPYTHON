"""

Graphs  are very useful data structures in solving any important mathematical challlenges

Types of graphs  Traversal
1 Depth First Traversal
2 Breadth First Traversal
https://www.tutorialspoint.com/python_data_structure/python_graph_algorithms.htm


"""
#example of  Depth First Traversal

class graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = {}
      self.gdict = gdict
# Check for the visisted and unvisited nodes
def dfs(graph, start, visited = None):
   if visited is None:
      visited = set()
   visited.add(start)
   print(start)
   for next in graph[start] - visited:
      dfs(graph, next, visited)
   return visited

gdict = { 
   "a" : set(["b","c"]),
   "b" : set(["a", "d"]),
   "c" : set(["a", "d"]),
   "d" : set(["e"]),
   "e" : set(["a"])
}
dfs(gdict, 'a')
            
            