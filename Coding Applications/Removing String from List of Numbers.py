
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