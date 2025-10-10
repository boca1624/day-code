class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, node1, node2):
        if node1 in self.adj_list:
            self.adj_list[node1].append(node2)
        else:
            self.adj_list[node1] = [node2]

        # Ensure bidirectional edges
        if node2 in self.adj_list:
            self.adj_list[node2].append(node1)
        else:
            self.adj_list[node2] = [node1]

    def dfs_recursive(self, start_node):
        visited = set()

        def dfs(current_node):
            if current_node not in visited:
                visited.add(current_node)
                print(current_node, end=' ')
                for neighbor in self.adj_list.get(current_node, []):
                    dfs(neighbor)

        dfs(start_node)

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]

        while queue:
            current_node = queue.pop(0)
            if current_node not in visited:
                visited.add(current_node)
                print(current_node, end=' ')
                queue.extend(self.adj_list.get(current_node, []))

# Example usage:
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)

print("DFS (Recursive):")
graph.dfs_recursive(1)
print
