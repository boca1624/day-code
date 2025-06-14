from collections import defaultdict

def find_subarrays_with_sum_k(nums, k):
    """
    给定一个整数数组 nums 和一个整数 k，返回所有连续子数组的起止索引，
    这些子数组的和为 k。
    """
    prefix_sum = 0
    sum_indices = defaultdict(list)
    sum_indices[0].append(-1)  # 辅助处理从头开始的子数组
    result = []

    for i, num in enumerate(nums):
        prefix_sum += num
        if (prefix_sum - k) in sum_indices:
            for start_index in sum_indices[prefix_sum - k]:
                result.append((start_index + 1, i))
        sum_indices[prefix_sum].append(i)

    return result

# 示例调用
nums = [1, 2, 3, -2, 5, -3, 2]
k = 5
print(find_subarrays_with_sum_k(nums, k))
