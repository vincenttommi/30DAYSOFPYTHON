""""

this algorithm traverses a graph breadth ward  motion and uses  a queue to remember to get 
the next vertext start a search , when a  dead end occurs in any iteration.
"""


import collections

class graph:
    def __init__(self, dict=None):
        if dict is None:
            dict = {}
        self.dict =  dict    
def bfs(graph, startnode):
        #Track the visited and unvisited nodes using queue
        seen, queue = set([startnode]), collections.deque([startnode])
        while queue:
            vertex = queue.popleft()
            marked(vertex)
            for node in graph[vertex]:
                seen.add(node)
                queue.append(node)
                
def marked(n):
    print(n)
    
    
     #The graph dictionary
     
dict = { 
   "a" : set(["b","c"]),
   "b" : set(["a", "d"]),
   "c" : set(["a", "d"]),
   "d" : set(["e"]),
   "e" : set(["a"])
}
bfs(dict, "a")     