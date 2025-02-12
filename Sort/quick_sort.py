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
print(quick_sort(array))