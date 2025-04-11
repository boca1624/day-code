def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Example usage
nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # Output: 4
