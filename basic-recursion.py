"""countdown"""

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)

countdown(5)

"""sumlist"""

def sum_list(items):
    if len(items) == 1:
        return items[0]
    else:
        return items[0] + sum_list(items[1:])

sum_list([1, 2, 3, 4, 5])

"""fibonacci"""

def native_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    n_minus1 = native_fibonacci(n-1)
    n_minus2 = native_fibonacci(n-2)
    return n_minus1 + n_minus2
    

"""quicksort"""

def quicksort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]

    left = []
    right = []

    for current in data[1:]:
        if current <= pivot:
            left.append(current)
        elif current > pivot:
            right.append(current)

    return quicksort(left) + [pivot] + quicksort(right)


"""Matts code"""

# def partition(data):
#     # Partition the data
#     # Start by choosing a pivot (choose the first item in the list)
#     pivot = data[0]
#     # We need to create storage for the LHS and the RHS
#     left = []
#     right = []
# ​
#     # We need to loop through each item
#     for current in data[1:]:
#         # if it's smaller or equal, append to left
#         if current <= pivot:
#             left.append(current)
#         # if it's bigger, add to RHS storage
#         else:
#             right.append(current)
# ​
#     return left, right, pivot
# ​
# ​
# # What kind of input will we get?
# # We expect a list
# def quicksort(data):
#     # check if data has 1 or 0 elements
#     # (base case) a side only contains a single element
#     if len(data) <= 1:
#         return data
# ​
#     left, right, pivot = partition(data)
# ​
#     # (recursive case) Recursively Quick Sort LHS and RHS until
#     return quicksort(left) + [pivot] + quicksort(right)
# ​
# ​
# print(quicksort([2,5,7,1,3,4,6,9,8]))