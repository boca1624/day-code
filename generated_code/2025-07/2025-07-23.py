class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()
        visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
        return visited

    def is_connected(self):
        start_node = next(iter(self.graph))  # Get an arbitrary start node
        visited = self.dfs(start_node)
        return len(visited) == len(self.graph)

# 示例用法
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(4, 5)

print(g.is_connected())  # 输出是否是连通图
