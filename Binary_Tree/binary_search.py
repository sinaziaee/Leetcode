def recursive_binary_search(arr, val, left, right):
    if left > right:
        return -1
    
    mid = (left + right)//2
    if arr[mid] == val:
        return mid
    elif val < arr[mid]:
        return recursive_binary_search(arr, val, left, mid - 1)
    else:
        return recursive_binary_search(arr, val, mid + 1, right)

def binary_search(arr, val):
    left = 0
    right = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


nums = [-1,0,3,5,9,12]
target = 9
print(recursive_binary_search(nums, target, 0, len(nums)))
print(binary_search(nums, target))