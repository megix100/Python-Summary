
print("Generator=> Allows to reduce space in the memory")

def generator(num):
    for i in range(num):
        yield i
    #This function just saves in the memory instead of returning and stops the function until the command "next"
    # appears
# for item in generator(1000):
#     print(item)

#Instead of using the part at the top we can call the function choosing the element
g=generator(100)
print(g) #find the location in memory
print(next(g))#The command next allow to access the values stored in memory in an order - First Value
print(next(g)) #Second Value
print(next(g)) #Third Value
#if the range expires after we do many NEXTs, it is going to give us an Error

print("\nExercise Fibonacci Number")
def fib(number):
    a=0
    b=1
    for i in range(number):
        yield a
        temp=a
        a=b
        b=temp+b

for x in fib(20):
    print(x)




