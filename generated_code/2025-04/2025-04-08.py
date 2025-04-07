def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_first_and_last(nums, target):
    def search(nums, target, find_first):
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result = mid
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    first = search(nums, target, True)
    last = search(nums, target, False)
    return (first, last)

# Example Usage
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(find_first_and_last(nums, target))  # Output: (3, 4)
