def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# 示例：数组中有两个相同的数字和一个不同的数字
nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # 输出 4
