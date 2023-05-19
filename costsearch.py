class Graph_costsearch:
    def __init__(self, directed=True):
        self.graph = {}
        self.directed = directed

    def add_edge(self, node1, node2, weight=1):
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append((node2, weight))
        if not self.directed:
            if node2 not in self.graph:
                self.graph[node2] = []
            self.graph[node2].append((node1, weight))

    def cost_search(self, start, goals):
        frontier = [(0, start, [start])]
        visited = set()
        while frontier:
            (cost, node, path) = frontier.pop(0)
            if node not in visited:
                visited.add(node)
                if node in goals:
                    return (path, node)
                for (neighbor, weight) in self.graph[node]:
                    if neighbor not in visited:
                        total_cost = cost + weight
                        frontier.append((total_cost, neighbor, path + [neighbor]))
                frontier.sort()

        return (None, None)

    @staticmethod
    def print_path(path, goal):
        for node in path:
            print(node, end=' ')
            if node == goal:
                break
        print()
