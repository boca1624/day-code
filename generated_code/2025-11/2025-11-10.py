class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[v].append(u)  # Assuming undirected graph

    def dfs_recursive(self, node, visited):
        visited.add(node)
        print(node, end=' ')
        for neighbor in self.adj_list.get(node, []):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def dfs_iterative(self, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                stack.extend(reversed(self.adj_list.get(node, [])))

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend(self.adj_list.get(node, []))

# Example usage:
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge
