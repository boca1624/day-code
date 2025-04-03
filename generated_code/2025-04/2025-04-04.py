import heapq

def find_k_largest(nums, k):
    # 用最小堆来保持最大的k个元素
    if not nums or k == 0:
        return []
    
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    
    return min_heap

# 示例用法
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_k_largest(nums, k))  # 输出 [5, 6]
