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