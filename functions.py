## -------------------------- Functions --------------------------
'''
    - A function is a block of code which only runs when it is called.
    - You can pass data, known as parameters, into a function.
    - A function can return data as a result.
'''

# -------------------------- Creating a Function --------------------------

'''In Python a function is defined using the def keyword:'''
def m_sum():
    print("hello")

# -------------------------- Calling a Function --------------------------
'''To call a function, use the function name followed by parenthesis:'''

def m_sum():
    print("hello")

m_sum()

# -------------------------- Arguments --------------------------
'''
 - Information can be passed into functions as arguments.
 - 
 - Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
 - 
 - The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:'''

def d_sum(a,b):
    s = a + b
    print(s)

d_sum(20,30)


# --------------------------  Parameters or Arguments? --------------------------
'''The terms parameter and argument can be used for the same thing: information that are passed into a function.'''

'''
From a function's perspective:

    - A parameter is the variable listed inside the parentheses in the function definition.
    - An argument is the value that is sent to the function when it is called.
'''
# -------------------------- Arbitrary Arguments, *args --------------------------
'''If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:'''

def name(*fname) :
    print(fname)

name("daya","Ranju")

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

'''     Arbitrary Arguments are often shortened to *args in Python documentations.      '''

# Arbitrary Arguments are often shortened to *args in Python documentations.

'''You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.'''

def name(*fname,lname,mname):
    print("fname :", fname)
    print("lname :", lname)
    print("mname :", mname)

name(lname="Shankar", mname="M M")
''' The phrase Keyword Arguments are often shortened to kwargs in Python documentations. '''

# -------------------------- Arbitrary Keyword Arguments, **kwargs --------------------------
'''If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:'''

def name(**n):
    print("Fname is :",n["fname"])
    print("Lname is :",n["lname"])
    print("Mname is :",n["mname"])
    print("Fullname is :", n["fname"] + n["lname"] +" " +n["mname"])
name(fname="Daya", lname="Shankar", mname="M M")

''' Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations. '''

# -------------------------- Default Parameter Value --------------------------
'''The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:'''

def name(fname = "Daya"):
    print("Name is :", fname)

name("Ranju")

# -------------------------- Passing a List as an Argument --------------------------
'''You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:
'''
def f(z):
    for i in z:
        print(i)
food=["Eggs","Pizza","Birayni"]

f(food)

# -------------------------- Return Values --------------------------
'''To let a function return a value, use the return statement:'''

def mul(x):
    return x * 10

print(mul(2))
print(mul(5))
print(mul(10))

# -------------------------- The pass Statement v
'''function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.'''

def mul(x):
    pass

print(mul(2))

# Recursion
'''Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. 
It means that a function calls itself. 
This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. 
However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.'''

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


## --------------------------------  Pragrams ------------------------------------

# square and Cube

def square_cube(num):
   sqr = num ** 2
   cub = num ** 3
   return sqr, cub
out = square_cube(10)
print(out)                   ;''' Multiple output from function'''

# Sum of list

def list_sum(num):
   return(sum(num))         ; #sum is a inbuilt function for list

print(list_sum([1,2,3,4]))

# Mul of list
def m1(num):
   res = 1
   for i in num:
      res = res * i
   return res
l1 = [1, 2, 3]
print(m1(l1))

# Factorial of number

def fac(num):
    print(num)
    if num <= 1:
       return 1
    
    return num * fac(num - 1)

print(fac(0))

# -------------------------------- MAP --------------------------------

''' The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.'''

''' Syntax
            map(function, iterables)

Parameter Values
    Parameter	Description
    function	Required. The function to execute for each item
    iterable	Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable.'''

def l(name):
   return len(name)

x = map(l, ("Daya", "Ranju", "Shankar"))
print(x)
print(list(x))

# Make new fruits by sending two iterable objects into the function:
def n(a,b):
   return a + b
x = map(n, ('Ranjitha ',), ('D Shankar',))
print(list(x))

# cube of number
def cube(a):
      return a ** 3
x = map(cube, (2, 3, 4))
print(list(x))




# -------------------------------- filter() --------------------------------
'''  The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.'''
'''
    Syntax
        filter(function, iterable)

    Parameter Values
    Parameter	Description
    function	A Function to be run for each item in the iterable
    iterable	The iterable to be filtered
'''
# even numbers
def even(n):
   return n % 2 == 0

numb = list(range(1, 50))

print(list(filter(even, numb)))

# Filter the array, and return a new array with only the values equal to or above 18:
def num(l):
   return l >= 18
l = list(range(1, 30))
print(list(filter(num, l)))

# -------------------------------- reduce() --------------------------------
from functools import reduce
def addition(x , y):
   return x + y
l = range(1, 10)
print(reduce(addition, l))

