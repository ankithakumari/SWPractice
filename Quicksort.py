# Quick sort - partition using last element as pivot

nums = [10, 20, 40, 80, 90, 50, 70]

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1  #Holds the index to smaller elements
    for j in range(low, high): #excluding the pivot element
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    #Place the pivot in its position
    arr[i+1],arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

quicksort(nums, 0, len(nums)-1)
print(nums)




