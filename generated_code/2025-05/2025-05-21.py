def maxProfit(prices):
    # dp[i][0] - the maximum profit on day i with no stock in hand
    # dp[i][1] - the maximum profit on day i with a stock in hand
    dp = [[0, -prices[0]] for _ in range(len(prices))]
    
    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])  # No stock today, max profit from either holding or selling
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])  # Stock today, max profit from either holding or buying
    
    return dp[-1][0]  # Return max profit with no stock in hand on the last day

# Example usage:
prices = [1, 7, 3, 5, 10, 3, 9]
print(maxProfit(prices))  # Output: 12
