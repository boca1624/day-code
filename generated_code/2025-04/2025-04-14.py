def twoSum(nums, target):
    # 使用哈希表存储数组元素和对应的索引
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return None

# 示例
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # 输出 [0, 1]
