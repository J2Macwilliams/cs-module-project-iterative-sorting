# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        
        smallest_index = i
        # TO-DO: find next smallest element
        # loop thru from next index 
        for x in range(i+1, len(arr)):
            # compare all the remaining elements
            if arr[smallest_index] > arr[x]:
                # increment cur-index which is tied to smallest index
                smallest_index = x

        # Swap the found min element with the first element
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # establish n as global variable
    n = 0
    # create an overall loop
    while n < len(arr) - 1:
        # create a for loop that checks thru
        for i in range(len(arr) - 1):
            # establish comparable value j
            j = i + 1
            # compare values
            if arr[i] > arr[j]:
                # swap values
                arr[i], arr[j] = arr[j] , arr[i]

        # increment n
        n += 1
    
    # return sorted array
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Create dictionary
    counts = {}
    # loop thru array
    for num in arr:
        # add to dictionary if not num
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        if num not in counts:
            counts[num] = 0
        # increment counter
        counts[num] += 1
    
    # create new sorted array
    sorted_array = []
    # loop through sorted counts dictionary items
    for n, count in sorted(counts.items()):
        # loop thru quantity of each count
        for i in range(count):
            # append number to sorted array
            sorted_array.append(n)
    # return array
    return sorted_array
