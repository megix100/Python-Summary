# Creating a List out of a String
print("Both LIST AND SET are almost the same, the only thing that changes is the {set} to [list]")
print("Creating a List out of a String")
li1 = []
for char in 'hello':
    li1.append(char)
se1=set(li1)
print(se1)

print("\nEasier way to do the same")
se2 = {char for char in 'hello'}  # Structure: variable FOR variable IN iterable
se2=sorted(se2)
print(se2)

print("\nAnother Example with Numbers")
se3 = {num for num in range(0, 100)}
print(se3)

print("\nHowever the situation above is less efficiency than the one below with numbers")
se4 = set(range(0, 100))
print(se4)

print("\nYou could use a map function, but the situation below is MORE efficient")
print("Double each number in a list that is going to be created")
se5 = {num ** 2 for num in range(0, 100)}
print(se5)

print("\nThis is something much easier to do with List Comprehension")
print("Double Each number and CHECK IF IT IS AN EVEN NUMBER BEFORE ADD TO THE LIST")
print("\n{num ** 2 for num in range(0, 100) if num % 2 == 0}")
print("(ACTION) + (        LOOP        ) + (CONDITIONAL)\n")
se6 = {num ** 2 for num in range(0, 100) if num % 2 == 0}
#      (ACTION) + (        LOOP        ) + (CONDITIONAL)
print(se6)

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