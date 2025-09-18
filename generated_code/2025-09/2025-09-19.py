class Solution:
    def find_min_subset_sum(self, arr, k):
        arr.sort()
        left, right = 0, len(arr) - 1
        subset_sum = 0
        while left <= right and k > 0:
            if arr[left] + arr[right] <= k:
                subset_sum += arr[left] + arr[right]
                left += 1
                right -= 1
            elif arr[left] + arr[right] > k:
                right -= 1
            k -= 1
        return subset_sum if k == 0 else -1
