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
