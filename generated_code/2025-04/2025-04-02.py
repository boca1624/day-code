class Solution:
    def merge(self, left, right):
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left or right)
        return result
    
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(left, right)

# 示例使用
nums = [38, 27, 43, 3, 9, 82, 10]
solution = Solution()
print(solution.mergeSort(nums))
