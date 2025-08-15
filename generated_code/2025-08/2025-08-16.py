class Solution:
    def find_min_cost_to_connect_islands(self, grid):
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        parent = list(range(m * n))
        rank = [0] * (m * n)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                            union(i * n + j, nx * n + ny
