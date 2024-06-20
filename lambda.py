# ------------------------------ Lambda ------------------------------
'''
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
'''
# Syntax
#lambda arguments : expression
# The expression is executed and the result is returned:

x = lambda a: a + 5
print(x(5))

#Lambda functions can take any number of arguments:

x = lambda a, b: a * b
print(x(10, 2))

# Why Use Lambda Functions?
'''The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:'''

def myfunc(n):
    print(n)
    return lambda a : a * n
db = myfunc(2)
print(db(5))


countries = ['India', 'sl', 'usa', 'germany']

x = map(lambda a : a.upper(), countries)
print(list(x))
