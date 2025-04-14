def maxSlidingWindow(nums, k):
    from collections import deque
    result = []
    dq = deque()

    for i in range(len(nums)):
        # Remove indices that are out of the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements from the deque
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Once the window is formed, add the max element to the result
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
