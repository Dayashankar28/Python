### String concatination 

fname = "Chinnu"
lname = "Munnu Shankar"
print("Full name is : ",fname + " " + lname )
cname = fname + " " + lname 

# Length of the string
fname = "Chinnu"
lname = "Munnu Shankar"
print("Full name is : ",fname + " " + lname )
cname = fname + " " + lname 

print(f''' Length of {fname} is ''', len(fname))
print(f''' Length of {lname} is ''', len(lname))
print(f''' Length of {cname} is ''', len(cname))

# Upper and lowercase
name = "Chinnu Munnu Shankar"

print("name in uppercase",name.upper())
print("name in lowercase",name.lower())

# Str replace
name = "Chinnu Munnu Shankar"
print(name)
name = name.replace("Chinnu", "Ranjitha")
print(name)
name = name.replace('Munnu', 'D')
print(name) 

# Str Split
text = "Python is awesome"
words = text.split("P")
print("Words:", words)

#Slice From the Start (Range)
text = "Python is awesome"
print(text[0:5])   #O/p is Pytho ---> starting from 0 and 5 is excluded

# #Slice To the End
# By leaving out the end index, the range will go to the end:

text = "Python is awesome"
print(text[5:])   #O/p is Pytho ---> starting from 5 to end


# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Example
# Get the characters: From: "o" in "World!" (position -5) To, but not included: "d" in "World!" (position -2):

b = "Python is awesome"
print(b[-5:])


#Remove Whitespace 
#   The strip() method removes any whitespace from the beginning or the end:
b = " Python is awesome   "
print(b.strip())

b = " Python is awesome   "
print(b.lstrip())  # left strip

b = " Python is awesome   "
print(b.rstrip()) # right strip

## Zero Padding
n = "90"
print(n.zfill(4))

## end with pattren

news = ''' Try to insert the missing part to make the code work as expected'''
print(news.endswith("expected"))  #### o/p will be true or false

news = ''' Try to insert the missing part to make the code work as expected123'''
print(news.endswith("expected123"))  #### o/p will be true or false