def merge_sort(array):
    if len(array) == 1:
        return array
    inx = len(array) // 2
    left = merge_sort(array[:inx])
    right = merge_sort(array[inx:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

array = [61, 23, 32, -19, 78, 23, 25, 0]
print(merge_sort(array))