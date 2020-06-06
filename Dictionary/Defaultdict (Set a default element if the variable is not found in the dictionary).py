from collections import Counter, defaultdict, OrderedDict
#Collection is a module full of useful modules

print("\ndefaultdict Function")
print("allows to set a default element if the variable you are looking for in a dictionary was not found avoiding an error and putting an expression if desired")
my_d=defaultdict(int,{
    "a":1,
    "b":2,
    "c":3
}) #With the int, it is going to appear 0 if not found
print(my_d["d"])

my_di=defaultdict(lambda: 5,{
    "a":1,
    "b":2,
    "c":3
}) #With lambda: 5 it is going to appear 5 if not found
print(my_di["d"])

my_dic=defaultdict(lambda: "Not found mate",{
    "a":1,
    "b":2,
    "c":3
}) #With lambda: "Not found mate" it is going to appear "Not found mate" if not found
print(my_dic["d"])




