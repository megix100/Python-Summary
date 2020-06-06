print("Dictionary Comprehension")
print("Doubling numbers out of a dictionary value")
simple_dict= {'a': 1,
              'b': 4,
              'c': 6,
              'd': 9}
my_dict1={key:value**2 for key,value in simple_dict.items()}
print("""
REMEMBER:
Two Points=> key:value
Comma=> key, value
Items=> simple_dict.items
Parenthesis=> simple_dict.items()
""")
print(my_dict1)

print("\nDouble Each number and CHECK IF IT IS AN EVEN NUMBER BEFORE ADD TO THE LIST")
print("\n{key:value**2 for key,value in simple_dict.items() if value%2==0}")
print("  (   ACTION   ) + (               LOOP             ) + (CONDITIONAL)\n")
my_dict2={key:value**2 for key,value in simple_dict.items() if value%2==0}
print(my_dict2)

print("\nCreate a Dictionary out of a List and Double its numbers")
my_dict3={num:num**2 for num in [1,2,3,4,5,6]}
print(my_dict3)