def singleNumber(nums):
    # 使用异或运算，两个相同的数异或结果为 0，最终结果就是只出现一次的数
    result = 0
    for num in nums:
        result ^= num
    return result
