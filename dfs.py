class Graph_dfs:
    def __init__(self, directed=True):
        self.graph = {}
        self.directed = directed

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append(node2)
        if not self.directed:
            if node2 not in self.graph:
                self.graph[node2] = []
            self.graph[node2].append(node1)

    def depth_first_search(self, start, goals):
        visited = set()
        stack = [(start, [start])]
        while stack:
            (node, path) = stack.pop()
            if node not in visited:
                visited.add(node)
                if node in goals:
                    return (path, node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))
        return (None, None)

    @staticmethod
    def print_path(path, goal):
        for node in path:
            print(node, end=' ')
            if node == goal:
                break
        print()
