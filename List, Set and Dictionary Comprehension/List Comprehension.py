# Creating a List out of a String
print("Both LIST AND SET are almost the same, the only thing that changes is the {set} to [list]")
print("Creating a List out of a String")
li1 = []
for char in 'hello':
    li1.append(char)
print(li1)

print("\nEasier way to do the same")
li2 = [char for char in 'hello']  # Structure: variable FOR variable IN iterable
print(li2)

print("\nAnother Example with Numbers")
li3 = [num for num in range(0, 100)]
print(li3)

print("\nHowever the situation above is less efficiency than the one below with numbers")
li4 = list(range(0, 100))
print(li4)

print("\nYou could use a map function, but the situation below is MORE efficient")
print("Double each number in a list that is going to be created")
li5 = [num ** 2 for num in range(0, 100)]
print(li5)

print("\nThis is something much easier to do with List Comprehension")
print("Double Each number and CHECK IF IT IS AN EVEN NUMBER BEFORE ADD TO THE LIST")
print("\n[num ** 2 for num in range(0, 100) if num % 2 == 0]")
print("(ACTION) + (        LOOP        ) + (CONDITIONAL)\n")
li6 = [num ** 2 for num in range(0, 100) if num % 2 == 0]
#      (ACTION) + (        LOOP        ) + (CONDITIONAL)
print(li6)

print("\nBEST SOLUTION => Checking what are the Duplicates, PUT THEM IN ORDER")
li3=['a','d','n','m','n','b','c','b',]
duplicates3={char for char in li3 if li3.count(char)>1} #A set was created
duplicates4=list(duplicates3)
duplicates4.sort()
print(duplicates4)

print("\nBEST SOLUTION => Removing Duplicates from the list and putting them in order, PUT THEM IN ORDER")
li4=['a','b','c','b','d','n','m','n']
duplicates5=[char for char in li4 if li4.count(char)==1] #A set was created
duplicates6=list(duplicates3)+duplicates5
duplicates6.sort()
print(duplicates6)


print("\nREMOVING STRING FROM A LIST OF NUMBERS")
my_list = [1, 2, "a", "b", 3, "c"]

#Solution A
def filter_list1(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]
print(filter_list1(my_list))

#Solution B
def filter_list2(l):
  'return a new list with the strings filtered out'
  return [x for x in l if type(x) is not str]
print(filter_list2(my_list))

#Solution C
def filter_list3(l):
    new_list =[]
    for x in l:
        if type(x) != str:
            new_list.append(x)
    return new_list
print(filter_list3(my_list))

#Solution D
def filter_list4(l):
    return [item for item in l if isinstance(item,int)]
print(filter_list4(my_list))