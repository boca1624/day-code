def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0] * n
    dp[0], dp[1] = cost[0], cost[1]
    
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    
    return min(dp[-1], dp[-2])

# 示例
cost = [10, 15, 20, 25, 30, 5]
print(minCostClimbingStairs(cost))
