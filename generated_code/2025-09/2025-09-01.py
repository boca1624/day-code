class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, node1, node2):
        if node1 not in self.adj_list:
            self.adj_list[node1] = []
        if node2 not in self.adj_list:
            self.adj_list[node2] = []
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)

    def dfs_recursive(self, start):
        visited = set()
        self._dfs_recursive(start, visited)
        return visited

    def _dfs_recursive(self, node, visited):
        visited.add(node)
        for neighbor in self.adj_list.get(node, []):
            if neighbor not in visited:
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
