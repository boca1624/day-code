class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # Assuming undirected graph

    def dfs_recursive(self, start):
        visited = set()
        self._dfs_recursive(start, visited)
        return visited

    def _dfs_recursive(self, node, visited):
        if node not in visited:
            visited.add(node)
            for neighbor in self.adj_list[node]:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                queue.extend(self.adj_list[node])
        return visited
