from collections import Counter, defaultdict, OrderedDict
#Collection is a module full of useful modules

print("\nOrdereddict Function")
print("put an order in the dictionary function, so the order matters in it. The order you put is going to be maintained")
my_d=OrderedDict({
    "a":1,
    "b":2,
    "c":3
})
print(my_d)

my_di=OrderedDict({
    "c":3,
    "b":2,
    "a":1
})
print(my_di)
if my_d!=my_di:
    print("They are not equal")
else:
    print("They are equal")


