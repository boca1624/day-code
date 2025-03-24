from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()
        visited.add(node)
        print(node, end=" ")

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def connected_components(self):
        visited = set()
        components = []

        for node in self.graph:
            if node not in visited:
                component = []
                self._dfs_collect(node, visited, component)
                components.append(component)

        return components

    def _dfs_collect(self, node, visited, component):
        visited.add(node)
        component.append(node)

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs_collect(neighbor, visited, component)

# 示例使用
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(4, 5)

print("DFS Traversal starting from node 0:")
g.dfs(0)
print("\nConnected components in the graph:")
print(g.connected_components())
