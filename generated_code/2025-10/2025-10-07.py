def rotate_array(nums, k):
    n = len(nums)
    k %= n
    nums[:] = nums[-k:] + nums[:-k]
