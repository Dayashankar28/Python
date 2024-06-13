 ######## Python Loops ######

''' --> while loops
    --> for loops
'''

## The while Loop
'''With the while loop we can execute a set of statements as long as a condition is true.'''
i = 2
while i <= 20:
    print(i)
    i += 2

'''The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
'''
## -----------  The break Statement -----------

'''With the break statement we can stop the loop even if the while condition is true:
'''

i = 1
while i < 100 :
    print(i)
    if i == 10 :
        break
    i+= 1

    ###
