from collections import Counter, defaultdict, OrderedDict
#Collection is a module full of useful modules

li=[1,2,3,4,5,6,7,7,8,8,8,9,10,9,11,9,12,9]
st="Hey dude how are you doing today?"

print("Counter Function")
print("Count the number of elements and create a dictionary putting the ones with more elements at the front")
count=Counter(li)
print(count)
print(Counter(st))