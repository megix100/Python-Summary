print("Zip Function")
print("Put together two iterables, for examples: link two lists together")
first_list = [1, 2, 3]
second_list = (9, 6, 3)  # It can put lists, tuples, sets together
third_list = [7, 10, 8]
print(list(zip(first_list, second_list, third_list)))

print("Sorting with the second element")
a=[(0,2),(9,9),(10,-1),(4,3)]
b=a[:] #Copying list A keeping it intact
a.sort(key=lambda x:x[1]) #Sorting by the second member of the List
b.sort() #Sorting by the first member of the list
print(a)
print(b)