from collections import defaultdict

def find_subarrays_with_sum(nums, target):
    prefix_sum = 0
    count = 0
    prefix_count = defaultdict(int)
    prefix_count[0] = 1  # Base case: sum of 0 has one occurrence

    for num in nums:
        prefix_sum += num
        if (prefix_sum - target) in prefix_count:
            count += prefix_count[prefix_sum - target]
        prefix_count[prefix_sum] += 1

    return count

# 示例用法
nums = [1, 2, 3, -2, 5]
target = 5
print(find_subarrays_with_sum(nums, target))  # 输出满足子数组和为5的子数组个数
