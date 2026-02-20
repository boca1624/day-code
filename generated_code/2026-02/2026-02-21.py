def permute(nums):
    """
    生成一个数组的所有排列组合
    使用递归和回溯算法实现
    """
    def backtrack(first=0):
        # 当所有元素都被固定时，添加到结果中
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            # 动态维护数组
            nums[first], nums[i] = nums[i], nums[first]
            # 递归下一个元素
            backtrack(first + 1
