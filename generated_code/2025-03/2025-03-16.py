def singleNumber(nums):
    # 利用异或运算，两个相同的数异或结果为 0，异或所有数，最后剩下的就是那个只出现一次的数字
    result = 0
    for num in nums:
        result ^= num
    return result

# 示例输入
nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # 输出 4
