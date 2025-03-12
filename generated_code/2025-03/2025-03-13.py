def singleNumber(nums):
    # 通过位运算找出只出现一次的数字
    res = 0
    for num in nums:
        res ^= num
    return res
