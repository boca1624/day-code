def permute(nums):
    def backtrack(start=0):
        if start == len(nums):
            res.append(nums[:])
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  # Swap to create permutation
            backtrack(start + 1)  # Recurse
            nums[start], nums[i] = nums[i], nums[start]  # Backtrack (restore state)

    res = []
    backtrack()
    return res

# Example usage
nums = [1, 2, 3]
print(permute(nums))
