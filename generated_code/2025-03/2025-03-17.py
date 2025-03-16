def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0

    left_min = [0] * n
    right_max = [0] * n

    left_min[0] = prices[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], prices[i])

    right_max[n-1] = prices[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], prices[i])

    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, right_max[i] - left_min[i])

    return max_profit
