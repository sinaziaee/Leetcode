def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
    return array


array = [61, 23, 32, -19, 78, 23, 25, 0]
print(bubble_sort(array))