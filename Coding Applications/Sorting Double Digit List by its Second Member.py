print("Sorting with the second element")
a=[(0,2),(9,9),(10,-1),(4,3)]
b=a[:] #Copying list A keeping it intact
a.sort(key=lambda x:x[1]) #Sorting by the second member of the List
b.sort() #Sorting by the first member of the list
print(a)
print(b)