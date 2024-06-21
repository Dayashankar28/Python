#What is a Module?
'''Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.
'''
#Create a Module
'''To create a module just save the code you want in a file with the file extension .py:

ExampleGet your own Python Server
Save this code in a file named mymodule.py
'''

# Use a Module
'''Now we can use the module we just created, by using the import statement:
'''
import mymodule
mymodule.welcome("Ranju")

mymodule.add(5,0)
mymodule.sub(5,3)

# --------------------- Variables in Module
'''The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):'''

import mymodule

a = (mymodule.person1)
for i, j in a.items():
    print(i, j)