class Solution:
    def find_min_path(self, grid):
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        dp = [[float('inf')] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]
        
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                from_top = grid[i][j] + dp[i-1][j] if i > 0 else float('inf')
                from_left = grid[i][j] + dp[i][j-1] if j > 0 else float('inf')
                dp[i][j] = min(from_top, from_left)
                
        return dp[-1][-1]
