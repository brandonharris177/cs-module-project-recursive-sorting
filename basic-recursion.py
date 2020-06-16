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
