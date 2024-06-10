#                               Set
'''--> A set is a collection which is unordered, unchangeable*, and unindexed.
Note: Sets are unordered, so you cannot be sure in which order the items will appear.

--->Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

---> Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Once a set is created, you cannot change its items, but you can remove items and add new items.

---> Duplicates Not Allowed
Sets cannot have two items with the same value.'''

#Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Set Items - Data Types
'''Set items can be of any data type:'''
set1 = {"abc", 34, True, 40, "male"}
print(type(set1))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Access Set Items ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
'''
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

#Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)  # true or flase

#Check if "banana" is NOT present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset) # true or flase

# ------------------------------------------ Add Set Items ------------------------------- 

'''Once a set is created, you cannot change its items, but you can add new items.'''

'''To add one item to a set use the add() method.'''
s1 = {"apple", "banana", "cherry"}
s1.add("strawberrys")
print(s1)

#Add Sets
''' To add items from another set into the current set, use the update() method '''
#1
s1 = {"apple", "banana", "cherry"}
s2 = {"pineapple", "mango", "papaya"}
s1.update(s2)
print(s1)
print(len(s1))

#2
s1 = {"apple", "banana", "cherry"}
s2 = ["Daya", 32, "Male"]
s1.update(s2)
print(s1)
print(len(s1))

# ------------------------------------------ Remove Set Items ------------------------------- 

'''To remove an item in a set, use the remove(), or the discard() method. '''

thisset = {"apple", "banana", "cherry"}
print("Before : ", thisset)
thisset.remove("banana")
print("After : ", thisset)

#Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}
print("Before : ", thisset)
thisset.discard("ba")
thisset.discard("banana")
print("After : ", thisset)

#The clear() method empties the set:
#The del keyword will delete the set completely:

#------------------------------ Loop Sets -----------------------

thisset = {"apple", "banana", "cherry"}
for i in thisset :
    print(i)


# ------------------------------------------- Join Sets -----------------------------------------
'''
--> There are several ways to join two or more sets in Python.

--> The union() and update() methods joins all items from both sets.

--> The intersection() method keeps ONLY the duplicates.

--> The difference() method keeps the items from the first set that are not in the other set(s).

--> The symmetric_difference() method keeps all items EXCEPT the duplicates. '''

#Union
'''The union() method returns a new set with all items from both sets.'''

set1 = {"a", "b", "c"}
set2 = {1, "b", 3}

set3 = set1.union(set2)
print(set3)

#You can use the | operator instead of the union() method, and you will get the same result.

set1 = {"a", "b", "c"}
set2 = {1, "b", 3}

set3 = set1 | set2
print(set3)

#Join Multiple Sets

'''
All the joining methods and operators can be used to join multiple sets.

When using a method, just add more sets in the parentheses, separated by commas: '''

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

result = set1.union(set2, set3, set4)
print(len(result))

# When using the | operator, separate the sets with more | operators:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

result = set1 | set2 | set3 | set4
print(len(result))

### ------------- Join a Set and a Tuple -------------------   ##

''' The union() method allows you to join a set with other data types, like lists or tuples. '''

x = {"a", "b", "c"}
y = (1, 2, "c")

result = x.union(y)
print(result)

# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

# Update Set

''' 
--> The update() method inserts all items from one set into another.
--> The update() changes the original set, and does not return a new set
'''

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Intersection
'''
--> Keep ONLY the duplicates
--> The intersection() method will return a new set, that only contains the items that are present in both sets.'''

set1 = {"a", "b" , "c", "h", "i", "j"}
set2 = {"a", "b" , "c", "d", "e", "f"}

set3 = set1.intersection(set2)
print(set1)

## You can use the & operator instead of the intersection() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# The intersection_update() method will also keep ONLY the duplicates, 
# but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

# Note : The values True and 1 are considered the same value. The same goes for False and 0.

# ------------------------ Difference -----------------------------
'''The difference() method will return a new set that will contain only the items from the first set that are not present in the other set. '''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3=set2.difference(set1)
print(set3)

## You can use the - operator instead of the difference() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

# The difference_update() method will also keep the items from the first set that are not in the other set, 
# but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)

# -------------------------- Symmetric Differences
'''The symmetric_difference() method will keep only the elements that are NOT present in both sets.
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

#------------------- Set Methods ---------------------------
''' Python has a set of built-in methods that you can use on sets.

    Method	Shortcut	Description

    add()	 	Adds an element to the set
    clear()	 	Removes all the elements from the set
    copy()	 	Returns a copy of the set
    difference()	-	Returns a set containing the difference between two or more sets
    difference_update()	-=	Removes the items in this set that are also included in another, specified set
    discard()	 	Remove the specified item
    intersection()	&	Returns a set, that is the intersection of two other sets
    intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
    isdisjoint()	 	Returns whether two sets have a intersection or not
    issubset()	<=	Returns whether another set contains this set or not
        <	Returns whether all items in this set is present in other, specified set(s)
    issuperset()	>=	Returns whether this set contains another set or not
        >	Returns whether all items in other, specified set(s) is present in this set
    pop()	 	Removes an element from the set
    remove()	 	Removes the specified element
    symmetric_difference()	^	Returns a set with the symmetric differences of two sets
    symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
    union()	|	Return a set containing the union of sets
    update()	|=	Update the set with the union of this set and others '''

