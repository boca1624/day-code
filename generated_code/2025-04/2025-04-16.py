def merge_sort(arr):
    # 分治算法：将数组分成两半，递归排序，再合并
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # 递归左半部分
    right = merge_sort(arr[mid:])  # 递归右半部分

    return merge(left, right)

def merge(left, right):
    # 合并两个已排序的数组
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 如果有剩余元素，直接加到结果中
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# 示例
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)
