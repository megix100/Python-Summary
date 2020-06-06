import random
#Find external modules here:
#https://docs.python.org/3/py-modindex.html

print(random)
help(random) #Describe what the module does
print(dir(random)) #Describe all the functions inside that module
print(random.random()) #Print a Random number
print(random.randint(1,10)) #Print a Random Integer between two numbers
print(random.choice([1,2,3,4,5,6,7])) #Makes a choice between the values you put there
my_list=[1,2,3,4,5,6,6,7,8,]
random.shuffle(my_list) #DON'T PUT PRINT, Shuffle will mix up the values of a list
print(my_list)