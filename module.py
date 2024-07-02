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

# Naming a Module
'''You can name the module file whatever you like, but it must have the file extension .py
'''
#Re-naming a Module
'''You can create an alias when you import a module, by using the as keyword:
'''
#Example
'''Create an alias for mymodule called mx:
'''
import mymodule as p

a = p.person1
for i in a.items():
    print(i)

# ------------------------------------ Built-in Modules ------------------------------------
'''There are several built-in modules in Python, which you can import whenever you like.
'''
#Example
#Import and use the platform module:

import platform

x = platform.system()
print(x)

# -------------------------------- Using the dir() Function --------------------------------
'''There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
'''
#Example
'''List all the defined names belonging to the platform module:
'''
import platform
import mymodule

x = dir(platform)
print(x)

y = dir(mymodule)
print(y)

import os
x = os.getcwd()
print(x)

os.system('rm -rf d')

# ------------------- products using api ----------------

import json
import requests

response = requests.get('https://fakestoreapi.com/products')
print(response)
products = json.loads(response.text)
print(type(products))
print(len(products))

def check_ele(data):
    if data['category'] == 'electronics':
        return data


ele_data = list(filter(check_ele, products))
print(len(ele_data))
