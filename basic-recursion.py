def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)

countdown(5)

def sum_list(items):
    if len(items) == 1:
        return items[0]
    else:
        return items[0] + sum_list(items[1:])

sum_list([1, 2, 3, 4, 5])