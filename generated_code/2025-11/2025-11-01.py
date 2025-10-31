class Solution:
    def find_min_cost_to_cut_rope(self, n, cuts):
        cuts.sort()
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            max_cost = 0
            for j in range(len(cuts)):
                if cuts[j] >= i:
                    max_cost = max(max_cost, dp[i - cuts[j]])
            dp[i] = max_cost + 1
        return dp[n]

# Example usage:
# n = 10
# cuts = [2, 3, 5, 7]
# print(Solution().find_min_cost_to_cut_rope(n, cuts))
