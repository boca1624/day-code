def maxSubArray(nums):
    # 使用动态规划来解决最大子数组和问题
    # dp[i]表示以nums[i]结尾的最大子数组和
    if not nums:
        return 0
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    max_sum = dp[0]

    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
        max_sum = max(max_sum, dp[i])
    
    return max_sum
