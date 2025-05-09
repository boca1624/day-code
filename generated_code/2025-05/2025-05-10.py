from typing import List

def find_disappeared_numbers(nums: List[int]) -> List[int]:
    """
    给定一个包含 [1, n] 之间所有数字的数组，其中一些数字出现了一次，有些出现了两次。
    找出所有没有出现在数组中的数字。
    要求不能使用额外空间且时间复杂度为 O(n)。
    """
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] *= -1

    result = [i + 1 for i, num in enumerate(nums) if num > 0]
    return result

# 示例
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_disappeared_numbers(nums))  # 输出: [5, 6]
