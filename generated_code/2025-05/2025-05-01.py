def singleNumber(nums):
    # 使用位运算解决找出数组中只出现一次的数字
    result = 0
    for num in nums:
        result ^= num
    return result

# 示例使用
nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # 输出 4
