from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def has_cycle(self):
        visited = set()
        rec_stack = set()

        def dfs(node):
            if node in rec_stack:
                return True
            if node in visited:
                return False
            visited.add(node)
            rec_stack.add(node)
            for neighbor in self.adj[node]:
                if dfs(neighbor):
                    return True
            rec_stack.remove(node)
            return False

        for node in self.adj:
            if dfs(node):
                return True
        return False


# 示例用法
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)  # 添加一个环

print("Graph has cycle:", g.has_cycle())  # 应输出 True
