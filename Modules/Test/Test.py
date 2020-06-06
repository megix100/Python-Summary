print(__name__)# Dunder method to print the name of this file in the parent file (modules.py)
def greetings():
    print("hello")

def action():
    item=(input("What action you want?"))
    print(f"Item being printed: {item}")

def grand_finale():
    print("Thank you Champs")

def add(x,y):
	try:
		if x and y:
			return int(x)+int(y)
		else:
			print("It has to be a number")
	except ValueError:
		print("This value must be a integer")

def sub(x,y):
	return x-y

def mult(x,y):
	return x*y

def divide (x,y):
	return x/y

print(add(5,6))
