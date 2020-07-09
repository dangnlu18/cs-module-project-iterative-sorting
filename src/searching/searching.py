from math import floor

def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here

    start_index = 0
    end_index= len(arr)-1
    found = False
    while not found:
        mid = floor((start_index + end_index)/2)
        if arr[mid] == target:
            found = True
            return mid
        else:
            if arr[mid] > target:
                end_index = mid-1
            if arr[mid] < target:
                start_index = mid+1
        return -1  # not found
