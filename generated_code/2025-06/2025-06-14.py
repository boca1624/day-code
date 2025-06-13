from collections import defaultdict, deque

class Graph:
    def __init__(self, num_nodes):
        self.graph = defaultdict(list)
        self.num_nodes = num_nodes

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def has_cycle(self):
        visited = [0] * self.num_nodes  # 0 = unvisited, 1 = visiting, 2 = visited

        def dfs(node):
            if visited[node] == 1:
                return True  # cycle found
            if visited[node] == 2:
                return False  # already processed

            visited[node] = 1
            for neighbor in self.graph[node]:
                if dfs(neighbor):
                    return True
            visited[node] = 2
            return False

        for i in range(self.num_nodes):
            if visited[i] == 0:
                if dfs(i):
                    return True
        return False

# 示例用法
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)  # 引入一个环

print(g.has_cycle())  # 输出: True
