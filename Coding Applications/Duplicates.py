print("REMOVING OR SHOWING DUPLICATES - PART ONE")

print("Checking what are the Duplicates and putting them in order")
li=['a','b','c','b','d','n','m','n']
duplicates1=[]
for item in li:
    if li.count(item)>1 and item not in duplicates1:
        duplicates1.append(item)
        duplicates1.sort()
print(duplicates1)

print("\nRemoving Duplicates from the list and putting them in order")
li1=['a','b','c','b','d','n','m','n']
duplicates2=[]
for item in li1:
    if item not in duplicates2:
        duplicates2.append(item)
        duplicates2.sort()
print(duplicates2)

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


print("COUNT ELEMENTS THAT APPEAR MORE THAN ONCE - PART TWO")
# def duplicate_count():
#     text=input("Choose a word or a text: ")
#     text=text.lower()
#     l=[]
#     for item in text:
#         if text.count(item)>1 and item not in l:
#             l.append(item)
#             print(f"The letter {item} appears {text.count(item)} times")
# duplicate_count()


def duplicate_count(text):
    text=text.lower()
    l=[]
    for item in text:
        if text.count(item)>1 and item not in l:
            l.append(item)
            print(f"The letter {item} appears {text.count(item)} times")
duplicate_count("HeLllllOooooO")
    # Your code goes here