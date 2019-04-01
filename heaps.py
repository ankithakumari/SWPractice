from time import time
# Heap implemented as an array

# Min heap has the least value in its roots as compared to its children
# for an item at i - 2i + 1 and 2i + 2 are its children, i-1/2 is the parent
def min_heap(heap, item):
        heap.append(item)
        i = len(heap) - 1 # index of inserted element
        while i > 0:
            p = (i - 1) // 2
            if heap[i] < heap[p]: # check if current element is less than its parent
                heap[i], heap[p] = heap[p], heap[i] # swap
            i = p

# Build a max heap - value at root greater than its children

def max_heap(heap, item):
    heap.append(item)
    i = len(heap) - 1
    while i > 0:
        p = (i - 1)// 2
        if heap[i] > heap[p]:
            heap[i], heap[p] = heap[p], heap[i]
        i = p

# n - size of array/heap
# root_index - index of root

def heapify(arr, n, root_index):
    largest = root_index
    left = 2 * root_index + 1  # left child
    right = 2 * root_index + 2  # right child
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right     # at this point the largest index is max of left and right child
    if largest != root_index:   # if root is not the largest, swap
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        heapify(arr, n, largest) # moves the largest element of the array to root



def buildmaxheap(arr):
    n = len(arr)
    for i in range(n, -1, -1):  # i goes from 6 to 0, decrementing by 1, calling heapify with every element as root
        heapify(arr, n, i)

def heapsort(arr):
    buildmaxheap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):  # index goes from 5 to 1 as last element in 0th index will be the min value
        arr[i], arr[0] = arr[0], arr[i]  # swap root element with last element of heap
        heapify(arr, i, 0)  # heap size decreases by 1 as we move largest elements to end of array

def extractlargest(arr):
    ret_val = arr.pop(0)        # Largest element is at root
    heapify(arr, len(arr), 0)   # call heapify to maintain the max heap property
    return ret_val

# Get kth largest element in an array

def getlargest(arr, k):
    buildmaxheap(arr)                           # Build max heap and extract k largest elements
    result = []
    for i in range(k):
        result.append(extractlargest(arr))
    return result

def minheapify(arr, n, root_index):
    smallest = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != root_index:
        arr[root_index], arr[smallest] = arr[smallest], arr[root_index]
        minheapify(arr, n, smallest)            # recursively move smallest element to the root

def ksmallest(arr, k):
    n = len(arr)
    for i in range(n, -1, -1):
        minheapify(arr, n, i)       # call minheapify n times
    result = []
    for i in range(k):
        result.append(arr.pop(0))
        minheapify(arr, len(arr), 0)
    return result


arr = list(reversed(range(1, 100))) # Descending array passed for a min heap - worst case
n = len(arr)
start = time()
for i in range(n, -1, -1):
    minheapify(arr, n, i)
end = time()
print(end - start)
# print(arr)