import heapq

def find_k_most_frequent(nums, k):
    # Step 1: Count frequencies
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Step 2: Use a min-heap of size k to keep top k frequent elements
    min_heap = []
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Step 3: Extract elements from the heap
    result = [num for freq, num in min_heap]
    return result

# 示例用法
nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
k = 2
print(find_k_most_frequent(nums, k))  # 输出: [1, 4] 或 [4, 1]
