def find_unique_triplet(nums):
    """
    在一个整数数组中，除了一个数字只出现一次外，其余每个数字都出现了三次。
    使用位运算在 O(n) 时间复杂度和 O(1) 空间复杂度内找出只出现一次的数字。
    """
    ones, twos = 0, 0
    for num in nums:
        # 首先将出现第二次的数字加入到twos中
        twos |= ones & num
        # 然后将出现第一次的数字加入到ones中
        ones ^= num
        # 出现三次的数字会在ones和twos中都出现一次
        # 把这些数字清除掉
        common_mask = ~(ones & twos)
        ones &= common_mask
        twos &= common_mask
    return ones


# 示例用法：
nums = [5, 3, 5, 3, 5, 3, 42]
print(find_unique_triplet(nums))  # 输出应为 42
