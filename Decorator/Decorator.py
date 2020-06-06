print("Decorator")
print("Used to add features or boost multiple functions")

print("\nThis decorator below just works with functions without arguments")
def my_decorator(func):
    def wrap_func():  # This part is where you can add features before and/or after your function
        print("***********")
        func()
        print("***********")
    return wrap_func  # IMPORTANT THERE IS NO () AFTER

@my_decorator
def hello():
    print('Hey dude')

hello()

print("\nThe best thing is to always add arguments in the decorator just in case the function has it")
def my_decorator(func):
    def wrap_func(*args, **kwargs):  # This part is where you can add features before and/or after your function
        print("***********")
        func(*args, **kwargs)
        print("***********")
    return wrap_func  # IMPORTANT THERE IS NO () AFTER

@my_decorator
def hello(greeting="hi", emoji=":)", shout="duude"):
    print(greeting, emoji, shout)

hello("hi sir")


print("\n Using Decorator to measure the PERFORMANCE or TIME that takes for the machine to execute a code")
from time import time

def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f"It took {t2 - t1} s to perform this code")
    return wrap_func

@performance #YOUR CODE TO MEASURE THE PERFORMANCE GOES AFTER THIS LINE
def tot():
    total = 0
    for i in range(1000000):
        total += 5 * i
    print(total)

tot()


# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
print("\nCreating Authenticator")
user1 = {
    'name': 'Sorna',
    'valid': True
}

user2 = {
    'name': 'Fabio',
    'valid': True
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']: #Search the first element from all the arguments and then from Valid inside the keys of this argument and see if it is True
        fn(*args, **kwargs)
  return wrapper

@performance
@authenticated
def message_friends(user):
    print(f'message has been sent by {user["name"]}')

message_friends(user1)
message_friends(user2)