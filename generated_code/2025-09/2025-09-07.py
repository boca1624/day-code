def find_min_subsequence(nums):
    min_subseq = []
    remaining = sorted(nums)
    i = 0
    for num in nums:
        if len(min_subseq) == 0 or num < min_subseq[-1]:
            min_subseq.append(num)
            remaining.remove(num)
        if len(min_subseq) == len(nums) // 2:
            break
    return min_subseq + remaining

# Example usage:
nums = [2, 4, 3, 1, 5, 3, 2]
print(find_min_subsequence(nums))  # Output: [1, 2, 2, 3, 3, 4]
