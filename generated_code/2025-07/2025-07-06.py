import heapq

def kth_largest(nums, k):
    # 创建一个最小堆来维持前 k 大的元素
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    
    return min_heap[0]

# 示例
nums = [3,2,1,5,6,4]
k = 2
print(kth_largest(nums, k))  # 输出: 5
