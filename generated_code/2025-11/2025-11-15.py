import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

def find_k_largest_elements(arr, k):
    return heapq.nlargest(k, arr)

def find_k_smallest_elements(arr, k):
    return heapq.nsmallest(k, arr)

def validate_heap(h):
    return all(h[i] >= 2 * h[i + 1] for i in range(len(h) // 2))

def heapify_array(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapq._sift_down(arr, i, n)
    return arr
