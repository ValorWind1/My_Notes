import random

"""
Sorting algorithms:
bubble sort: stable, in-place, O(n^2)
selection sort: stable, in-place, O(n^2)
insertion sort: stable, in-place, O(n^2)
quick sort: unstable, in-place, O(nlogn)
merge sort: stable, out-of-place, O(nlogn)
heap sort: unstable, in-place, O(nlogn)
bucket sort: stable, O(n+k)
counting sort: stable, O(n+k)
radix sort: stable, O(nk)
"""

# generate 300 random integers in the range of -150 to 150
testCase = [random.randint(-150, 150) for x in range(300)]
print("Test case:\n", testCase)

"""
Sorts an unsorted sequence by comparing and swapping the adjacent pairs.
Its time complexity is O(n^2) and it is stable and in-place.
"""

def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap elements
    return arr

##bubble = bubbleSort(testCase)
##print("-" * 100)
##print("Bubble sort:\n", bubble)

"""
Sorts an unsorted sequence by selecting the minimum element in the remaining
sequence and swapping if they are in the wrong order. The algorithm
compares n^2 times but only swaps n times. The time complexity is still O(n^2).
It is stable and in-place.
"""

def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        minIdx = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIdx]: minIdx = j
        arr[minIdx], arr[i] = arr[i], arr[minIdx]
    return arr

##selection = selectionSort(testCase)
##print("-" * 100)
##print("Selection sort:\n", selection)

"""
Sorts an unsorted sequence by inserting the next element at the proper
position. Even the time complexity is still O(n^2), it's suitable for almost
sorted sequences. It is stable and in-place.
"""

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        marked = arr[i]
        j = i
        while j > 0 and arr[j - 1] > marked:
            arr[j] = arr[j - 1]  # shift
            j -= 1
        arr[j] = marked  # insert
    return arr

##insertion = insertionSort(testCase)
##print("-" * 100)
##print("Insertion sort:\n", insertion)

""" 
Sorts the unsorted sequence by using quick sort. Partitioning is done in place.
A randomized pivot is used. The time complexity is O(nlogn).
Height of tree is O(logn). Partitioning takes O(n). Quick sort is not stable.
"""

def quickSort(arr, start, end):
    if start >= end: return arr
    arr, left = partition(arr, start, end)
    quickSort(arr, start, left - 1)
    quickSort(arr, left + 1, end)
    return arr

def partition(arr, start, end):
    # generate a random pivot
    pIndx = random.randint(start, end - 1)
    # place the pivot at the end
    arr[pIndx], arr[end] = arr[end], arr[pIndx]
    # get the pivot
    pivot = arr[end]
    # get two pointers left and right
    left, right = start, end - 1
    while left <= right:
        while left <= right and arr[left] < pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    # insert the pivot into the right place
    arr[left], arr[end] = arr[end], arr[left]
    return arr, left

##quick = quickSort(testCase, 0, len(testCase) - 1)
##print("-" * 100)
##print("Quick sort:\n", quick)

"""
Sorts the unsorted sequence by using merge sort. Merge sort is
out-of-place but stable. The complexity is O(nlogn).
Height of tree is O(logn). Merging takes O(n). Merge sort is stable.
"""

def mergeSort(arr):
    n = len(arr)
    if n < 2: return arr
    # find the middle element
    mid = int(n / 2)
    # divide into two sub-lists
    arrLeft = arr[:mid]
    arrRight = arr[mid:]
    # merge sort recursively 
    mergeSort(arrLeft)
    mergeSort(arrRight)
    return merge(arrLeft, arrRight, arr)

# merge results
def merge(arrLeft, arrRight, arr):
    # two cursors i and j
    i = j = 0
    while i + j < len(arr):
        if j == len(arrRight) or (i < len(arrLeft) and arrLeft[i] < arrRight[j]):
            arr[i + j] = arrLeft[i]
            i += 1
        else:
            arr[i + j] = arrRight[j]
            j += 1
    return arr

##merge = mergeSort(testCase)
##print("-" * 100)
##print("Merge sort:\n", merge)

""" 
Heap sorts uses a heap to sort an array. First find the maximum element
and place the maximum element at the end. Repeay the same process
for remaining elements. The complexity is O(nlogn).
""" 

def heapify(arr, n, i):
    # n: size of heap
    largest = i # index of the parent
    l = 2 * i + 1 # index of the left child = 2 * i + 1 
    r = 2 * i + 2 # index of the right child = 2 * i + 2 
    # if i has a left child and is greater than its parent 
    if l < n and arr[i] < arr[l]: 
        largest = l
    # if i has a left child and is greater than the current largest
    if r < n and arr[largest] < arr[r]: 
        largest = r 
    # update root if children > parent
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i] # swap 
        # repeat same thing for a child
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    # create a max heap: root is current max
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for j in range(n - 1, 0, -1):
        arr[j], arr[0] = arr[0], arr[j] # swap elements
        heapify(arr, j, 0) # restore heap order for the root
    return arr

##heap = heapSort(testCase)
##print("-" * 100)
##print("Heap sort:\n", heap)

""" 
Bucket sort is mainly useful when input is uniformly distributed over a range.
Set up an array of initially empty "buckets". 
Scatter: go over the original array, putting each object in its bucket.
Sort: sort each bucket.
Concatenate: join each bucket together.
The complexity is O(n + k) where n is the size of the sequence and k is
the number of buckets.
"""

def bucketSort(arr, N):
    n = len(arr)
    # size of buckets
    ns = int(N/2)
    ps = N - ns
    negMAX = min(arr)
    posMAX = max(arr)
    # create N empty buckets 
    neg = list([] for i in range(ns))
    pos = list([] for i in range(ps))
    # put elements into different buckets
    for i in range(n):
        if arr[i] < 0:
            bi  = int(arr[i] * (ns - 1) / negMAX) # index of the bucket
            neg[bi].append(arr[i])
        else:
            bi  = int(arr[i] * (ps - 1) / posMAX) # index of the bucket
            pos[bi].append(arr[i])
    # sort individually
    for i in range(ns):
        neg[i] = insertionSort(neg[i])
    for i in range(ps):
        pos[i] = insertionSort(pos[i])
    # concatenate all buckets into arr
    arr_neg = list(neg[ns - i - 1][j] for i in range(ns) for j in range(len(neg[ns - i - 1])))
    arr_pos = list(pos[i][j] for i in range(ps) for j in range(len(pos[i])))
    return arr_neg + arr_pos 

##bucket = bucketSort(testCase, 50)
##print("-" * 100)
##print("Bucket sort:\n", bucket)

""" 
Counting sort is a sorting technique based on keys
between a specific range. It works
by counting the number of objects
having distinct key values (kind of hashing).
Then doing some arithmetic to calculate
the position of each object in the output sequence.
The complexity is O(n+k) where n is the size of the sequence
and k is the range of input. 
"""

def countingSort(arr): 
    # the output list that will have sorted sequence 
    output = [0] * len(arr) # initial values are all zeros
    MAX = max(arr) # find the max element
    MIN = min(arr) # find the min element
    # create a count list to store the number of occurence  
    # of each element, initialize count list as 0 
    count = [0] * (MAX - MIN + 1) # there are MAX - MIN + 1 counts
    # store count of each element
    for e in arr: count[e - MIN] += 1
    # calculate count[i] so that count[i] now contains actual 
    # position of this element in output
    for i in range(1, len(count)): count[i] += count[i-1] 
    # build the output  
    for i in range(len(arr)): 
        output[count[arr[i] - MIN]-1] = arr[i] # locate the element
        count[arr[i]- MIN] -= 1 # decrease the count by 1
    return output 

##counting = countingSort(testCase)
##print("-" * 100)
##print("Counting sort:\n", counting)

"""
Radix sort is a non-comparative integer sorting algorithm that sorts data
with integer keys by grouping keys by the individual digits
which share the same significant position and value.
Radix sort starts from least significant digit to most significant digit.
The complexity is O(nk) where n is the size of the sequence and k is
the average length of an element. 
"""

def digitCountingSort(arr, exp): 
    # the output list that will have sorted sequence 
    output = [0] * len(arr) # initial values are all zeros 
    # create a count list to store the number of occurence  
    # of each element, initialize count list as 0 
    count = [0] * 10 # there are 10 counts
    # store count of each element
    for i in range(0, len(arr)): 
        index = (arr[i] / exp) 
        count[int(index) % 10] += 1
    # calculate count[i] so that count[i] now contains actual 
    # position of this element in output
    for i in range(1, 10): count[i] += count[i-1] 
    # build the output
    i = len(arr) - 1
    while i >= 0:
        index = arr[i] / exp
        output[count[int(index) % 10] - 1] = arr[i] 
        count[int(index) % 10] -= 1
        i -= 1
    return output

def radixSort(arr):
    arrPos = [elem for elem in arr if elem >= 0]
    arrNeg = [elem for elem in arr if elem < 0]
    # find the maximum number to know number of digits 
    MAX = max(arr)
    MIN = min(arr)
    # repeat counting sort for every digit
    exp = 1
    while MAX / exp > 0:
        arrPos = digitCountingSort(arrPos, exp)
        exp *= 10
    exp = 1
    while abs(MIN) / exp > 0:
        arrNeg = digitCountingSort(arrNeg, -exp)
        exp *= 10
    arrNeg.reverse()
    return arrNeg + arrPos
    
##radix = radixSort(testCase)
##print("-" * 100)
##print("Radix sort:\n", radix)



    


