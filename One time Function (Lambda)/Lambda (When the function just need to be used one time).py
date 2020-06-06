from functools import reduce

print("Lambda Function")
print("When a function just need to be used one time, so it doesn't occupy space in the memory")
print("""lambda item: item*2
      Receive the variable item and multiply it by 2
""")
li=[1,2,3,4,5,6,7,8,9,10,11,12]
print(list(map(lambda item: item**2,li)))

print(list(filter(lambda item: item%2==0,li)))

print(reduce(lambda acc, item: acc+item, li))

print("Sorting with the second element")
a=[(0,2),(9,9),(10,-1),(4,3)]
b=a[:] #Copying list A keeping it intact
a.sort(key=lambda x:x[1]) #Sorting by the second member of the List
b.sort() #Sorting by the first member of the list
print(a)
print(b)
