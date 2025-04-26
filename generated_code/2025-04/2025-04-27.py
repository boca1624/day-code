def singleNumber(nums):
    # 通过位运算找出数组中只出现一次的数字
    res = 0
    for num in nums:
        res ^= num
    return res

# 示例使用
nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # 输出 4
