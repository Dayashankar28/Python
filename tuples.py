#                                                   Tuple
'''A tuple is a data structure similar to a list, but unlike lists, tuples are immutable, meaning their contents cannot be changed after creation. Tuples are typically used for grouping related data.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

'''

# Create a Tuple:

thistuple = ("apple", "mango", "banana")
print(thistuple)
print(type(thistuple))

#Tuple Items
'''Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.'''

#Ordered
'''When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
'''

# Unchangeable
'''Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.'''

# Tuple Length
'''To determine how many items a tuple has, use the len() function:'''

thistuple = ("apple", "mango", "banana")
print(len(thistuple))

# Tuple Items - Data Types
''' Tuple items can be of any data type'''

'''A tuple with strings, integers and boolean values:'''

tuple1 = ("abc", 34, True, 40, "male")

#   Access Tuple Items
'''You can access tuple items by referring to the index number, inside square brackets'''

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1[3])

#Negative Indexing

'''
Negative indexing means start from the end.

-1 refers to the last item, -2 refers to the second last item etc.
'''
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1[-4])

#Range of Indexes
''' You can specify a range of indexes by specifying where to start and where to end the range.

    When specifying a range, the return value will be a new tuple with the specified items. '''

tuple1 = ("abc", 34, True, 40, "male", "abc", 34, True, 40, "male")
print(tuple1[2:8])

'''     Note: The search will start at index 2 (included) and end at index 5 (not included).    '''

# Update Tuples

    #Change Tuple Values
'''Once a tuple is created, you cannot change its values. 
   Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.'''

daya = ["Daya", 32, True, 40, "male"]
ranju = ["Ranju", 30, True, 40, "female"]
x = (daya, ranju )
y = list(x)
print(x)
y.append(["shankar", 32, True, 40, "male"])
x = tuple(y)
print(x)

#Add tuple to a tuple. 
'''You are allowed to add tuples to tuples, so if you want to add one item, (or many), 
create a new tuple with the item(s), and add it to the existing tuple:'''

t1 = ("Daya", 32, True, 40, "male")
t2 = ("Ranju", 30, True, 40, "female")
t1 += t2
print(t1)

#Remove Items
'''Tuples are unchangeable, so you cannot remove items from it, 
but you can use the same workaround as we used for changing and adding tuple items:
'''
t1 = ("Daya", 32, True, 40, "male", ("Ranju", 30, True, 40, "female"))
t2 = list(t1)
t2.pop(5)
t1 = tuple(t2)
print(t1)

#you can delete the tuple completely:
''' The del keyword can delete the tuple completely  '''

t1 = ("Daya", 32, True, 40, "male", ("Ranju", 30, True, 40, "female"))
print(t1)
del t1
print(t1)

#Unpack Tuples

'''we are also allowed to extract the values back into variables. This is called "unpacking"'''

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#Tuple Methods
'''Python has two built-in methods that you can use on tuples.

    Method	Description '''

'''--> count()	Returns the number of times a specified value occurs in a tuple
'''

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

'''--> index()	Searches the tuple for a specified value and returns the position of where it was found '''

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(7)
print(x)

