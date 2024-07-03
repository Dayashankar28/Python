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
import json, requests

def fetch_products():
    url = 'https://fakestoreapi.com/products'
    response = requests.get(url)
    return response.json()

def check_electronics(data):
    return data['category'] == 'electronics'

if __name__ == "__main__":
    products = fetch_products()
    print("Response status:", products)
    print("Type of products:", type(products))
    print("Number of products:", len(products))

    electronics_data = list(filter(check_electronics, products))
    print("Number of electronics products:", len(electronics_data))

# ------------------- number of repo ----------------

import json, requests, wget

def get_user_data():
    url = 'https://api.github.com/users/iam-veeramalla'
    response = requests.get(url)
    return response.json()
data = get_user_data()
print("Data type is : ", (type(data)))
print("Data len is : ", (len(data)))
Name = data.get("name")
followers = data.get("followers")
public_repos = data.get("public_repos")
print((type(json.dumps(data))))
#
#print(f'Name of the user is : {Name} \n Total number of followers is : {followers} \n number if respos is : {public_repos}')
######## --------------
filtered_dict = {key: data[key] for key in ['name', 'followers']}

print(filtered_dict)

##########

original_dict = {
  "name": "Abhishek Veeramalla",
  "company": "Red Hat",
  "blog": "www.youtube.com/@AbhishekVeeramalla",
  "location": "Hyderabad, India",
  "email": None,
  "public_gists": 8,
  "followers": 12468,
  "following": 1
}

filtered_dict = dict(filter(lambda item: item[0] in ['name', 'followers'], original_dict.items()))

print(filtered_dict)
