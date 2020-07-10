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
    while start_index <= end_index:
        mid = (start_index + end_index)//2
        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            end_index = mid-1
        else:
            start_index = mid+1
    return -1  # not found
