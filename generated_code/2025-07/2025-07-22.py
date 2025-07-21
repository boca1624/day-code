def twoSum(nums, target):
    # 使用哈希表存储已遍历的元素
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# 示例
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
