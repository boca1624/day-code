def permute(nums):
    def backtrack(start=0):
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  # Swap
            backtrack(start + 1)  # Recurse
            nums[start], nums[i] = nums[i], nums[start]  # Backtrack (undo swap)

    result = []
    backtrack()
    return result

# Example usage:
nums = [1, 2, 3]
print(permute(nums))
