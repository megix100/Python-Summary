print("Checking for e-mails")
import re
x=None
while x==None:
    validation = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    email = input("What is your e-mail? ")
    print(validation.search(email))  # If it is NONE=>It is not an e-mail
    x=validation.search(email)
    if x==None:
        print("You type a wrong e-mail.Please try it again")
else:
    print("thank you")