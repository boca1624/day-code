import heapq

def build_min_heap(data):
    heapq.heapify(data)
    return data

def extract_min_heap(data):
    return heapq.heappop(data)

def insert_into_heap(data, value):
    heapq.heappush(data, value)
    return data

def heap_sort(data):
    sorted_data = []
    heapified_data = build_min_heap(data)
    while heapified_data:
        sorted_data.append(extract_min_heap(heapified_data))
    return sorted_data
