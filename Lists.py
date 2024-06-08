#What is a List?
'''A list is a fundamental data structure in programming that allows you to store a collection of items. 
Lists are ordered and can contain elements of various data types, such as numbers, strings, and objects.'''

#creating List
my_list = [1, 2, 3, 'apple', 'banana'] # Lists are created using square brackets

#List Indexing
''' List elements are indexed, starting from 0 for the first element. 
You can access elements by their index. '''

my_list = [1, 2, 3, 'apple', 'banana']
print(f"Element from my_list is --> {my_list[4]}")

#reveres indexing
my_list = [1, 2, 3, 'apple', 'banana']
print(f"Element from my_list is --> {my_list[-3]}")
ele = my_list[-3]
print(type(ele))  #finding Datatype

# to fetch pattren of letter from list 
my_list = [1, 2, 3, 'apple', 'banana']
print(my_list[-2][-2])   # it will fetch apple and within apple L

# Changeable
''' The list is changeable, meaning that we can change, add, and remove items in a list after it has been created. ''''

#List Length
my_list = [1, 2, 3, 'apple', 'banana']
print(len(my_list))

#Access Items
''' List items are indexed and you can access them by referring to the index number '''

#Range of Indexes
'''You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items. '''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#Change List Item Value

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[0] = "grapes"
print(thislist)

#Change a Range of Item Values
''' To change the value of items within a specific range, define a list with the new values, 
and refer to the range of index numbers where you want to insert the new values '''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[0:3] = ["g1", "g2", "g2"]
print(thislist)

#Insert Items into the List
''' To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index '''

thislist = ["apple", "banana", "cherry"]
thislist.insert(1,"new")
print(thislist)

#Add List Items
        
        #Append Items
''' To add an item to the end of the list, use the append() method: '''

thislist = ["apple", "banana", "cherry"]
thislist.append("mango")
print(thislist)

        #Extend List
''' To append elements from another list to the current list, use the extend() method.'''

thislist1 = ["apple", "banana", "cherry"]
thislist2 = ["mango", "grapes", "berries"]

thislist1.extend(thislist2)
print(thislist1)

        #Add Any Iterable
'''The extend() method does not have to append lists, 
 you can add any iterable object (tuples, sets, dictionaries etc.)'''

thislist = ["apple", "banana", "cherry"]
thistuple = ("mango", 3, "cars", "456")

thislist.extend(thistuple)
print(thislist)
print(type(thislist))

# Remove List Items

        #Remove Specified Item
''' The remove() method removes the specified item '''

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

        #Remove Specified Index
''' The pop() method removes the specified index '''

thislist = ["apple", "banana", "cherry", "mango", "grapes", "berries"]
thislist.pop(1)
print(thislist)

        #Clear the List
''' The clear() method empties the list.

The list still remains, but it has no content '''

thislist = ["apple", "banana", "cherry", "mango", "grapes", "berries"]
print(len(thislist))
thislist.clear()
print(thislist, len(thislist))
