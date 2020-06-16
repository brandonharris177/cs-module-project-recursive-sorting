# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # print(elements)
    merged_arr = [0] * elements
    # print(merged_arr)
    current = 0
    # Your code here
    while current < len(merged_arr):
        # print(arrA)
        if len(arrA) == 0 and len(arrB) >= 1:
            merged_arr[current] = arrB[0]
            arrB.pop(0)
            current = current+1
            # print(merged_arr)
        elif len(arrB) == 0 and len(arrA) >= 1:
            merged_arr[current] = arrA[0]
            arrA.pop(0)
            current = current+1
            # print(merged_arr)
        elif arrA[0] <= arrB[0]:
            merged_arr[current] = arrA[0]
            arrA.pop(0)
            current = current+1
            # print(merged_arr)
        elif arrA[0] >= arrB[0]:
            merged_arr[current] = arrB[0]
            arrB.pop(0)
            current = current+1
            # print(merged_arr)
    # print(arrA, arrB)
    # print(merged_arr)
    return merged_arr

# merge([2, 4, 6, 8], [1, 3, 5, 7, 11, 13, 15])

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        # print(arr)
        return arr
    else:
        middle = len(arr) //2
        end = len(arr)
        smaller = merge_sort(arr[0: middle])
        larger = merge_sort(arr[middle: end])
        return merge(smaller, larger)

# merge_sort([2, 4, 6, 8, 1, 3, 5, 7, 11, 13, 15])

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


# def pop_test(arr):
#     print(arr)
#     arr.pop(0)
#     print(arr)

# pop_test()

