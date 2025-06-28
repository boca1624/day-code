class MergeSort:
    def sort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sort(nums[:mid])
        right = self.sort(nums[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

# 使用示例
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
merge_sort = MergeSort()
sorted_arr = merge_sort.sort(arr)
print(sorted_arr)
