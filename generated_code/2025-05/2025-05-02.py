from typing import List

def find_max_subarray_sum(nums: List[int], k: int) -> int:
    """
    在长度为 k 的滑动窗口内，找到最大子数组和。
    利用前缀和优化查找。
    """
    n = len(nums)
    if n < k:
        return -1

    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]

    max_sum = float('-inf')
    for i in range(k, n + 1):
        window_sum = prefix_sums[i] - prefix_sums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# 示例
nums = [2, 1, -3, 4, -1, 2, 1, -5, 4]
k = 4
print(find_max_subarray_sum(nums, k))  # 输出应为具有挑战性的窗口和
