# --------------  Dictionary  --------------------

'''
--> Dictionaries are used to store data values in key:value pairs.
--> A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
--> Dictionaries are written with curly brackets, and have keys and values:
'''

#Dictionary Items

'''Dictionary items are presented in key:value pairs, and can be referred to by using the key name '''
car = {
  "brand": "Tata",
  "model": "Altroz",
  "year": 2023
}
print(car["brand"])

# Changeable
'''Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.'''

# Duplicates Not Allowed
'''Dictionaries cannot have two items with the same key:
'''
# Duplicate values will overwrite existing values:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(car)

#Dictionary Length
#To determine how many items a dictionary has, use the len() function:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
print(len(car))


# --------------- Dictionary Items - Data Types  --------------- 

'''The values in dictionary items can be of any data type: '''

car = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(car["colors"]))

# --------------------------- Access Dictionary Items ---------------------------

#Accessing Items
'''You can access the items of a dictionary by referring to its key name, inside square brackets'''

# There is also a method called get() that will give you the same result:

car = {
  {"brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]},
  {"brand": "Tata",
  "electric": False,
  "year": 2000,
  "colors": ["red", "white", "blue"]}
}
print(car.get("brand"))

# -------------------- Get Keys --------------------
'''The keys() method will return a list of all the keys in the dictionary.'''
car = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(car.keys())

# Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
  "brand": "Ford",
  "electric": False,
  "year": 1964
}

x = car.keys()
print("before: ", x)
car["colors"] = "White"
print("after: ", x)

# -------------------------- Get Values --------------------------
'''The values() method will return a list of all the values in the dictionary.
'''
car = {
  "brand": "Ford",
  "electric": False,
  "year": 1964
}
print(car.values())

#Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
  "brand": "Ford",
  "electric": False,
  "year": 1964
}
x = car.values()
print("before",x)
car["year"] = 2020
print("After",x)

# Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
  "brand": "Ford",
  "electric": False,
  "year": 1964
}

car["colors"] = ["white", "red", "blue"]
print(car)

# ------------------  Get Items -----------------
'''The items() method will return each item in a dictionary, as tuples in a list.
'''
car = {
  "brand": "Ford",
  "electric": False,
  "year": 1964
}
car["colors"] = ["white", "red", "blue"]
print(car)
print(car.items())

#Example
'''Make a change in the original dictionary, and see that the items list gets updated as well: '''
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

''' Add a new item to the original dictionary, and see that the items list gets updated as well: '''

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
car["colors"] = ["white", "red", "blue"]
print(car)
print(car.items())

#---------------------------- Check if Key Exists ----------------------------

''' To determine if a specified key is present in a dictionary use the in keyword: '''
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

if "brand" in car :
    print(True)
else :
    print(False)
    
# ------------ Change Dictionary Items ------------ #

#Change Values
'''You can change the value of a specific item by referring to its key name:'''
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

car["year"] = 2024
print(car.items())

# Update Dictionary
'''The update() method will update the dictionary with the items from the given argument.
The argument must be a dictionary, or an iterable object with key:value pairs.'''

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print("before", car)
car.update({"year" : 2024})
print("After", car)

# ------------------------------------- Adding Items -------------------------

'''Adding an item to the dictionary is done by using a new index key and assigning a value to it:
'''
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

car["colors"] = ["white", "black", "grey"]
print(car)

# Update Dictionary
'''The update() method will update the dictionary with the items from a given argument.
If the item does not exist, the item will be added.'''

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

car.update({"year" : 2024})
car.update({"colors" : ["white", "black"]})
print(car)

# ---------------- Remove Dictionary Items -------------

''' The pop() method removes the item with the specified key name: '''

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car.pop("year")
print(car)

'''The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)'''

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"color": "white"
}

car.popitem()
print(car)

'''The del keyword removes the item with the specified key name: '''

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"color": "white"
}

del car["year"]
print(car)

''' The del keyword can also delete the dictionary completely: '''
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"color": "white"
}
print("Before :", car)
del car
print(car)

''' The clear() method empties the dictionary: '''

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"color": "white"
}

car.clear()
print(car)

# ---------- Loop Through a Dictionary ----------

''' You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.'''

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"color": "white"
}

for i in car :
    print(i)
#### ------------- You can also use the values() method to return values of a dictionary: -------------
thisdict = {
    "brand": "Ford", 
    "model": "Mustang", 
    "year": 1964
}
for x in thisdict.values():
    print(x)

# ------------ You can use the keys() method to return the keys of a dictionary: ----

thisdict = {
    "brand": "Ford", 
    "model": "Mustang", 
    "year": 1964
}

for i in thisdict.keys():
    print(i)

## ------------- Loop through both keys and values, by using the items() method: ----
car = {
    "brand": "Ford", 
    "model": "Mustang", 
    "year": 1964
}

car.update({"colors": ["white", "grey"]})

for i, j in car.items():
    print(i, j)

# ---------------------- Copy a Dictionary
'''You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().'''

car1 = {
    "brand": "Ford", 
    "model": "Mustang", 
    "year": 1964
}

car2 = car1.copy()
print(car2)

# Another way to make a copy is to use the built-in function dict().

car1 = {
    "brand": "Ford", 
    "model": "Mustang", 
    "year": 1964
}

car2 = dict(car1)
print(car2)

# ----------------- Nested Dictionaries
'''A dictionary can contain dictionaries, this is called nested dictionaries.'''
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  },
    "child4" : {
    "name" : "abc",
    "year" : 2011
  }

}
print(myfamily)

# -------------------- Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

fam = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3,
}
print(fam)

# --------------------- Access Items in Nested Dictionaries -----------------------

''' To access items from a nested dictionary, you use the name of the dictionaries, 
starting with the outer dictionary:'''
myfamily = {
    "child1" : {
      "name" : "Emil",
      "year" : 2004
    },
    "child2" : {
      "name" : "Tobias",
      "year" : 2007
    },
    "child3" : {
      "name" : ["Ranju", "Chinnu Munnu"],
      "year" : 1995
    },
      "child4" : {
      "name" : "abc",
      "year" : 2011
    }
}
print(myfamily)

print(myfamily["child3"]["name"])

### ---- Loop Through Nested Dictionaries ---
'''You can loop through a dictionary by using the items() method like this:
'''
myfamily = {
    "child1" : {
      "name" : "Emil",
      "year" : 2004
    },
    "child2" : {
      "name" : "Tobias",
      "year" : 2007
    },
    "child3" : {
      "name" : ["Ranju", "Chinnu Munnu"],
      "year" : 1995
    },
      "child4" : {
      "name" : "abc",
      "year" : 2011
    }
}
for i, obj in myfamily.items():
    print(i)

    for j in obj:
        print(j + ":",obj[j])

# --- Dictionary Methods -----

''' Python has a set of built-in methods that you can use on dictionaries.

  Method	Description
-->  clear()	Removes all the elements from the dictionary
-->  copy()	Returns a copy of the dictionary
-->  fromkeys()	Returns a dictionary with the specified keys and value
-->  get()	Returns the value of the specified key
-->  items()	Returns a list containing a tuple for each key value pair
-->  keys()	Returns a list containing the dictionary's keys
-->  pop()	Removes the element with the specified key
-->  popitem()	Removes the last inserted key-value pair
-->  setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
-->  update()	Updates the dictionary with the specified key-value pairs
-->  values()	Returns a list of all the values in the dictionary

'''