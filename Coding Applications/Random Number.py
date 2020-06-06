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

while True: #While there is a wrong answer the While will keep looping the code
    try:
        num=int(input("Guess a number from 1 to 10? "))
    except: #Error Notification - This handle ALL ERRORS THE SAME WAY
        print("It needs to be a number")
    else: #If there is NO error
        guess = random.randint(1, 10)
        print(guess)
        while num != guess:
            num = int(input("Guess a number from 1 to 10? "))
            if guess > num:
                print("You are close try it again. Hint: the number is higher than the one you picked")
            elif guess < num:
                print("You are close try it again. Hint: the number is lower than the one you picked")
        else:
            print("Congratulations")
            break

#Another way to do it:
from random import randint
# you will need to run this on your machine and not this website for the sys.argv to work!

answer = randint(1,10)

while True:
    try:
        guess = int(input(f'guess a number 1 to 10:  '))
        if  0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print('hey bozo, I said 1~10')
    except ValueError:
        print('please enter a number')
        continue

#Creating a function with the same result:
from random import randint
def guessing(guess,answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')

if __name__=="__main__":
    answer = randint(0, 10)
    while True:
        try:
            guess=int(input(f'guess a number 1 to 10:  '))
            if guessing(guess,answer)==True: #Or just if guessing(guess,answer)
                break
        except ValueError:
            print('please enter a number')