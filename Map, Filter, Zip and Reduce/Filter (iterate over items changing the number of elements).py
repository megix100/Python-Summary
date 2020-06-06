print("Filter Function")
print("Filter can be used to iterate and filter values reducing the number of elements in the list")


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, [1, 2, 3])))



