#----------------- Conditions and If statements -----------------#
'''
Python supports the usual logical conditions from mathematics:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b
    These conditions can be used in several ways, most commonly in "if statements" and loops.

'''
a = 130 
b = 90
c = 50

if a > b and a > c :
    print(f"A = {a} is greater then B = {b} and C = {c}")
elif b > a and b > c :
    print(f"B = {b} is greater then A = {a} and C = {c}")
else :
    print(f"C = {c} is greater then A = {a} and B = {b}")

# Indentation
'''Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
Other programming languages often use curly-brackets for this purpose.
'''
# If statement, without indentation (will raise an error):

a = 33
b = 200
if b > a:
print("c is greater than a") # you will get an error

# ------------------------ Elif ------------------------
'''The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
'''
a = 130 
b = 90
c = 150

if a > b and a > c :
    print(f"A = {a} is greater then B = {b} and C = {c}")
elif b > a and b > c :
    print(f"B = {b} is greater then A = {a} and C = {c}")

# ---------------------------- Else ----------------------------
'''The else keyword catches anything which isn't caught by the preceding conditions.
'''
a = 130 
b = 90
c = 150

if a > b and a > c :
    print(f"A = {a} is greater then B = {b} and C = {c}")
elif b > a and b > c :
    print(f"B = {b} is greater then A = {a} and C = {c}")
else :
    print(f"C = {c} is greater then A = {a} and B = {b}")

# Short Hand If
'''If you have only one statement to execute, you can put it on the same line as the if statement.'''
a = 30
b = 4
if a > b : 
    print("a is greater")

#Short Hand If ... Else
'''If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:'''
a = 10
b = 30
print("A is greater") if a > b else print("B is greater")

# --- This technique is known as Ternary Operators, or Conditional Expressions. ----

a = 330
b = 33
print("A") if a > b else print("=") if a == b else print("B")

# ------------- And -------------
'''The and keyword is a logical operator, and is used to combine conditional statements:'''
a = 330
b = 33
c = 0
if a > b and a > c :
    print(f"A = {a} is greater")
# ------------- Or -------------
'''The or keyword is a logical operator, and is used to combine conditional statements:'''
a = 330
b = 33333
c = 0

if a > b or a > c:
    print(f"A = {a} is greater")

# ------------- Not-------------
'''The not keyword is a logical operator, and is used to reverse the result of the conditional statement:'''
a = 10
b = 100

if not a > b :
    print(" a is not grater")

# ---------------------  Nested If ---------------------
'''You can have if statements inside if statements, this is called nested if statements.'''

a = 100
if a > 50 :
    print("grt 50")
    if a >= 100 :
        print (" grt or eq 100")
    else :
        print("less 100")

# ------------------- The pass Statement --------------------
'''if statements cannot be empty, but if you for some reason have an if statement with no content, 
put in the pass statement to avoid getting an error.    '''
a = 1011
b = 100
if  a > b :
    pass