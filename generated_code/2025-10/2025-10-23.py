def minCostClimbingStairs(cost):
    if len(cost) == 1:
        return 0
    dp = [0] * len(cost)
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, len(cost)):
        dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    return min(dp[-1], dp[-2])

def climbStairs(n):
    if n <= 2:
        return n
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
