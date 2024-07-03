import json, requests, wget

def get_raw_data():
    url = 'https://fakestoreapi.com/users'
    response = requests.get(url)
    return response.json()

raw_data = (get_raw_data())
print(type(raw_data))

#-----------   File Handling -----------

'Python has several functions for creating, reading, updating, and deleting files.'

'''The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.'''

# There are four different methods (modes) for opening a file:
'''
    - "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    - 
    - "a" - Append - Opens a file for appending, creates the file if it does not exist
    - 
    - "w" - Write - Opens a file for writing, creates the file if it does not exist
    - 
    - "x" - Create - Creates the specified file, returns an error if the file exists'''

        # In addition you can specify if the file should be handled as binary or text mode
'''
    - "t" - Text - Default value. Text mode
    - 
    - "b" - Binary - Binary mode (e.g. images) '''


#Syntax
'''To open a file for reading it is enough to specify the name of the file:
'''
open("README.md")
'''The code above is the same as:
'''
f = open("README.md", "rt")
#Because "r" for read, and "t" for text are the default values, you do not need to specify them.


#### opening and writing ( you need to close opened files)####
f = open("example.txt", "w")
i = open("README.md","w")
f.write("This is from file handling....")
i.write("This is from file handling....")
f.close()
i.close()

#### open and write without closeing ###

with open("example.txt", "w") as f1:
    f1.write("\n this is sentance two")
    
f = open(r"C:\Users\mmday\OneDrive\Documents\1.xlsx", "a")
f.write("jihjhkjjkhjkjkjkhNin masdsadka")
######