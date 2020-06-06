print(__name__)# Dunder method to print the name of this file in the parent file (modules.py)
def buy(item):
    cart=[]
    cart.append(item)
    print(cart)

if __name__=='__main__': #This sentence allows to identify which one is the main or parent module
#SO THIS SENTENCE IS NOT GOING TO RUN IF YOU EXECUTE THE modules.py file instead of this one
    print("This is the main module")