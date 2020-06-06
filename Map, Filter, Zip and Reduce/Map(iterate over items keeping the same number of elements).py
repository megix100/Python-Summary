# Multiplication
print("\nMultiplication Function")
def multi(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list
print(multi([1, 2, 3]))

print("\nMAP FUNCTION")
print("easier multiplication function using Map")
print("Map can be used every time you will iterate over to change something keeping the same number of items in the list")
def multiplication(item):
    return item * 2
print(list(map(multiplication, [1, 2, 3])))
