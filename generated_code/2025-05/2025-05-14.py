def find_two_unique_numbers(nums):
    """
    在一个整数数组中，除了两个数字只出现一次外，其它数字都出现了两次。
    使用位运算找出这两个只出现一次的数字。
    """
    xor = 0
    for num in nums:
        xor ^= num  # 最终结果是两个不同数字的异或结果

    # 找到xor中最低位的1，这个位在两个唯一数字中是不同的
    diff_bit = xor & -xor

    num1 = num2 = 0
    for num in nums:
        if num & diff_bit:
            num1 ^= num
        else:
            num2 ^= num

    return num1, num2

# 示例用法
nums = [4, 1, 2, 1, 2, 5]
print(find_two_unique_numbers(nums))  # 输出: (4, 5) 或 (5, 4)
