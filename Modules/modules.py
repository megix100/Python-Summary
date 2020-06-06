print(__name__) # Dunder method to show if this file is the MAIN or PARENT one (the name of the other files
# appearing because there are print(__name__) function on them too

from Modules.Shopping import shopping_cart #You need to create a Python Package

shopping_cart.buy("apple")

#you could also do the below in order to reduce the length of the code

from Modules.Shopping.shopping_cart import buy

buy("apple") #shorter function

#Getting more than one function using import (use comma ",")
from Modules.Test.Test import action,greetings
action()
greetings()

#Instead of getting multiple functions using comma "," use a star ("*")
from Modules.Test.Test import *
grand_finale()

if __name__=='__main__': #This sentence allows to identify which one is the main or parent module
#AND THIS FILE IS THE MAIN ONE IF YOU RUN THIS FILE AND NOT THE OTHER ONE
    print("This is the main module")