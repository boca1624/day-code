def depth_first_search(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            # 假设 graph 是一个字典，键是节点，值是邻居节点列表
            for neighbor in graph[vertex]:
                stack.append(neighbor)
    return visited

# 使用示例
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(depth_first_search(graph, 'A'))
