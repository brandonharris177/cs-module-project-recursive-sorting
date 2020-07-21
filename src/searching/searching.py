# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if len(arr) == 0:
        # print("-1")
        return -1
    
    mid = (start + end) // 2

    if arr[mid] == target: 
        # print(mid)
        return mid
    elif end < start:
        # print("-1")
        return -1 
    elif arr[mid] > target: 
        return binary_search(arr, target, start, mid - 1)  
    elif arr[mid] < target: 
        return binary_search(arr, target, mid + 1, end) 

# arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# binary_search(arr1, 6, 0, len(arr1))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
