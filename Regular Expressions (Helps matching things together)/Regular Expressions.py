import re
#https://www.w3schools.com/python/python_regex.asp
print("Searching for a word in a sentence- It says where it starts and ends")
string="Hello, this is Mr Pinkman, the biggest traitor. this is unfair"
a=re.search("this",string)
print(a)
print(a.span()) #The span shows where the word is starting and ending
print(a.start())
print(a.end())
print(a.group()) #The group converts the information from the Span to the actual word in that position

print("\n Instead of searching for one word all the time, you can change in the top everything with COMPILE")
pattern=re.compile("this")
b=pattern.search(string)
print(b)
c=pattern.findall(string) #Find how many times the word appears there
print(c)

print("\nCheck if both TEXTS are the EXACTLY THE SAME")
patt=re.compile("Hello, Mr Ciro could you please pass the salt?")
d=patt.fullmatch("Hello, Mr Ciro could you please pass the salt!")
#EVEN A SMALL DIFFERENCE - EXCLAMATION / INTERROGATION SIGNS WILL GET CAUGHT - And the RETURN IS NONE
print(d)
pat=re.compile("Hello, Mr Ciro could you please pass the salt")
e=pat.fullmatch("Hello, Mr Ciro could you please pass the salt")
#if it is equal then it is True
print(e)

# print("\nCheck if ons text is inside the other - It doesn't matter if there are things before or after")
# pa=re.compile("Hello, Mr Ciro could you please pass the salt")
# text="Hello, Mr Ciro could you please pass"
# f=pa.match(text)
# #if it is equal then it is True
# print(f)

print("\nChecking for e-mails")
validation=re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email=input("What is your e-mail? ")

print(validation.search(email)) #If it is NONE=>It is not an e-mail

def passwordStrength():
    while True:
        # Enter password text
        passwordText = input('Enter Password: ')

        # Strength Checks
        charRegex = re.compile(r'(\w{8,})')  # Check if password has atleast 8 characters
        lowerRegex = re.compile(r'[a-z]+') # Check if at least one lowercase letter
        upperRegex = re.compile(r'[A-Z]+')# Check if atleast one upper case letter
        digitRegex = re.compile(r'[0-9]+') # Check if at least one digit.

        ''' TODO: Enter conditions to see if password passes all checks and then return
        a message if it does.'''
        if charRegex.findall(passwordText) == []:  # Checks if the password does not contain 8 characters and returns a message
            print('Password must contain at least 8 characters')
        elif lowerRegex.findall(passwordText)==[]: # Checks if the password does not contain a lowercase character and returns a message
            print('Password must contain at least one lowercase character')
        elif upperRegex.findall(passwordText)==[]: # Checks if the password does not contain an uppercase character and returns a message
            print('Password must contain at least one uppercase character')
        elif digitRegex.findall(passwordText)==[]: # Checks if the password does not contain a digit character and returns a message
            print('Password must contain at least one digit character')
        else:  # if the above 4 conditions are successfully passed, pringt out a message saying the password is strong.
            print('Your password is strong. Good job!')
            break