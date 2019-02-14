import random

def selectionSort(arr):
    n = len(arr)
    for i in range(0, n):
        # find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        # swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        leftArr = arr[:mid]
        rightArr = arr[mid:]

        # Do mergesort on left and right
        mergeSort(leftArr)
        mergeSort(rightArr)

        i = j = k = 0
        # copy values into the original array
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                k+=1
                i+=1
            else:
                arr[k] = rightArr[j]
                k+=1
                j+=1
        # check for left out values
        while i < len(leftArr):
            arr[k] = leftArr[i]
            k+=1
            i+=1
        while j < len(rightArr):
            arr[k] = rightArr[j]
            k+=1
            j+=1

def quickSort(arr):
    start = 0
    end = len(arr) - 1
    quickSortHelper(arr, start, end)

def partition(arr, start, end):
    randNum = random.randint(0,len(arr))
    pivot  = arr[randNum]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[randNum] = arr[randNum], arr[i+1]
    return (i+1)

def quickSortHelper(arr, start, end):
    if start < end:
        partitionIndex = partition(arr, start, end)
        quickSortHelper(arr, start, partitionIndex -1)
        quickSortHelper(arr, partitionIndex + 1, end)


  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    quickSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 