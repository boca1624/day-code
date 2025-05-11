def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    # dp[i] 表示以 nums[i] 结尾的最长上升子序列的长度
    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # 返回 dp 数组中的最大值，即最长上升子序列的长度
    return max(dp)

# 示例输入
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print("最长上升子序列长度:", longest_increasing_subsequence(nums))
