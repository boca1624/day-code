class Solution:
    def searchRange(self, nums, target):
        def binarySearch(left, right, findFirst):
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    if findFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result
        
        first = binarySearch(0, len(nums) - 1, True)
        if first == -1:
            return [-1, -1]
        last = binarySearch(0, len(nums) - 1, False)
        return [first, last]
