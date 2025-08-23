def search_in_graph(graph, start, target):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node == target:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False
