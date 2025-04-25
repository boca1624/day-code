class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_util(self, v, visited):
        visited[v] = True
        result = [v]
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                result.extend(self.dfs_util(neighbor, visited))
        return result

    def dfs(self, start):
        visited = [False] * self.V
        return self.dfs_util(start, visited)


# Example usage
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

print(g.dfs(0))
