# Input : sorted array of distinct integers
# Output : magic index i, where arr[i] == i. Else if i doesnt exist, -1

# Use binary search approach 

def magicIndex(arr):
    if arr == None: 
        return -1
    low = 0
    high = len(arr) - 1
    return magicIndexHelper(arr, low, high)

def magicIndexHelper(arr, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        high = mid - 1
        return magicIndexHelper(arr, low, high)
    elif arr[mid] < mid:
        low = mid + 1
        return magicIndexHelper(arr, low, high)

# FOLLOW UP

# def magicIndexWithRepeats(arr):
#     if arr == None: 
#         return -1
#     low = 0
#     high = len(arr) - 1
#     return magicIndexWithRepeatsHelper(arr, low, high)

# def magicIndexWithRepeatsHelper(arr, low, high):
#     if low > high:
#         return -1
#     midIndex = (low + high) // 2
#     midValue = arr[midIndex]

    





print(magicIndexWithRepeats([1, 1, 1, 2, 3]))