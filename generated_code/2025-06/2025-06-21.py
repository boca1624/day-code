def nextPermutation(nums):
    # 找到倒序的第一个升序对
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    if i >= 0:
        # 找到比 nums[i] 大的最小数，交换
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    
    # 反转 i 后面的部分
    nums[i + 1:] = reversed(nums[i + 1:])
    return nums
