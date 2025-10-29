class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def dfs_recursive(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for i in self.graph[v]:
            if i not in visited:
                self.dfs_recursive(i, visited)

    def dfs_iterative(self, start):
        visited = set()
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                stack.extend(reversed(self.graph[vertex]))

# 使用示例
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print("DFS Recursive:")
graph.dfs_recursive(2, set())

print("\nDFS Iterative:")
graph.dfs_iterative(2)
