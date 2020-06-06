#This structure of While True, try, except and else is ALWAYS going to be the same

print("Handling ANY ERROR in the SAME WAY")
while True: #While there is a wrong answer the While will keep looping the code
    try:
        age=int(input("What is your age? "))
        print(age)
    except: #Error Notification - This handle ALL ERRORS THE SAME WAY
        print("It needs to be a number")
    else: #If there is NO error
        break #Breaks out of the loop or THE WHOLE REST OF THE PROGRAMMING CAN BE HERE

print("\nHandling TWO DIFFERENT ERRORS in the DIFFERENT WAYS")
while True: #While there is a wrong answer the While will keep looping the code
    try:
        num=int(input("What is your number? "))
        print(10/num)
    except ValueError: #Error Notification - This handle specifically the ERROR when the value IS NOT AN INTEGER
        print("It needs to be a number")
    except ZeroDivisionError: #Error Notification - This handle specifically the ERROR when the value IS 0
        print("It needs to be different from 0")
    else: #If there is NO error
        break #Breaks out of the loop or THE WHOLE REST OF THE PROGRAMMING CAN BE HERE

print("\nHandling Errors INSIDE A FUNCTION, STRING TO NUMBER and SHOWING SYSTEM DESCRIPTION")
def total():
    while True:  # While there is a wrong answer the While will keep looping the code
        try:
            num1 = int(input("What is your first number? "))
            num2 = int(input("What is your second number? "))
            print(num1 + num2)
        except (ValueError, TypeError) as error:  # Error Notification - This handle specifically the ERROR when the value IS A STRING
            #You could use ValueError OR TypeError instead of (ValueError, TypeError)
            #The error variable (it doesn't need to be called error) is going to show a description from the system that can be useful
            print(f"It needs to be a number not a string {error}")
        else:  # If there is NO error
            break  # Breaks out of the loop or THE WHOLE REST OF THE PROGRAMMING CAN BE HERE
total()

print("\nSame as the above, but with FINALLY function and counting the time of trials")
def total():
    i=0
    while True:  # While there is a wrong answer the While will keep looping the code
        try:
            num1 = int(input("What is your first number? "))
            num2 = int(input("What is your second number? "))
            print(num1 + num2)
        except (ValueError, TypeError) as error:  # Error Notification - This handle specifically the ERROR when the value IS A STRING
            #You could use ValueError OR TypeError instead of (ValueError, TypeError)
            #The error variable (it doesn't need to be called error) is going to show a description from the system that can be useful
            print(f"It needs to be a number not a string {error}")
            i+=1
            if i==1:
                print(f"You have tried it {i} time")
            else:
                print(f"You have tried it {i} times")
        else:  # If there is NO error
            break  # Breaks out of the loop or THE WHOLE REST OF THE PROGRAMMING CAN BE HERE

total()

print("""
THERE ARE TWO MORE FUNCTIONS NOT BEING SHOWN HERE, BECAUSE THEY ARE NOT OFTEN USED:
Finally and Raise Functions
Check Error Handling Chapter:
https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16077584#bookmarks 
""")