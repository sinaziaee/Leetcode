def merge_sort(array):
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[-1]
    left = []
    right = []
    for x in array[:-1]:
        if x <= pivot:
            left.append(x)
    for x in array[:-1]:
        if x > pivot:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)

array = [61, 23, 32, -19, 78, 23, 25, 0]
print("merge sort:", merge_sort(array))
print("quick sort:", quick_sort(array))

for i in range(len(array)-1, -1, -1):
    print(i)