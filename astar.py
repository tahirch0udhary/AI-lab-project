from collections import defaultdict
class Graph_astar:
    def __init__(self, directed):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, w):
        if self.directed:
            self.graph[u].append((v, w))
        else:
            self.graph[u].append((v, w))
            self.graph[v].append((u, w))

    def heuristic(self, node, goal):
        # implementation of heuristic function
        pass

    def astar_search(self, start, goal):
        # implementation of A* search algorithm
        pass
