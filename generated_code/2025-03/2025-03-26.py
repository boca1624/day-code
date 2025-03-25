def singleNumber(nums):
    # 利用位运算，异或所有数字，结果即为只出现一次的数字
    result = 0
    for num in nums:
        result ^= num
    return result
