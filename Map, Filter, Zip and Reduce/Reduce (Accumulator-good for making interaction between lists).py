from functools import reduce  # this part is needed for the reduce function

my_list = [1, 2, 3]  # needed
print("Reduce Function")
print("Good for making interactions betweend Lists - check the Map, Filter, Zip and Reduce (exercises) file")
def accumulator(acc, item):  # the name doesn't need to be accumulator, acc or item
    print(f'{acc}:{item}')  # part that it is not needed (it is just easier to understand with it
    return acc + item  # this part is needed but not necessarily a sum
print(reduce(accumulator, my_list, 0))
print(""""
reduce(accumulator, iterable, initial value of the accumulator)
Initial Value of the Accumulator(Acc0)         First Item
            0                                      1
            
New Value of the Accumulator(Acc1)            Second Item
    From Return Acc0+1=1                           2
    
New Value of the Accumulator(Acc2)            Second Item
    From Return Acc1+2=3                           3

Final Value=> Acc2+Second Item=3+3=6

""")
