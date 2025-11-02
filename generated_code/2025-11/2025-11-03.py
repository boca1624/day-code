class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[v].append(u)

    def dfs_recursive(self, start):
        visited = set()
        self._dfs_recursive(start, visited)
        return visited

    def _dfs_recursive(self, node, visited):
        if node not in visited:
            visited.add(node)
            for neighbor in self.adj_list.get(node, []):
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            current = queue.pop(0)
            for neighbor in self.adj_list.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited

    def is_bipartite(self):
        color = {}
        for node in self.adj_list:
            if node not in color:
                if not self._bipartite_dfs(node, color):
                    return False
        return True

    def _bipartite_dfs(self, node, color):
        if node in color:
            return color[node]
