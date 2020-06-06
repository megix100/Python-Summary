#To access the Python Library: File=> Setting=> Project:Projects=> Python Interpreter=> +=> Search=> Install

import pyjokes

dir(pyjokes)
help(pyjokes)
print(pyjokes.get_joke("en","all"))