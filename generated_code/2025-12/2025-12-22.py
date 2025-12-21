def majority_element(nums):
    def divide_and_conquer(left, right):
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        left_majority = divide_and_conquer(left,
