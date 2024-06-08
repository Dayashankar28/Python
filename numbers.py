#Numbers data type to practice

num1 = 2
num2 = 1.092
num3 = 10+30j
num4 = "100"

print(num1)
print(num2)
print(num3)
 # type: ignore

 ### to print / find  or to know  type of variable
print(num1,type(num1))
print(num2,type(num2))
print(num3,type(num3))
print(num4,type(num4))

### Division of two numbers

num1 = 10
num2 = 2
result = num1 / num2
print(f'''Division of  {num1} and {num2} is : ''', result)

# Modulus (Remainder)
num1 = 11
num2 = 2
reminder = num1 % num2
result = num1 / num2
print(f'''Reminder of  {num1} and {num2} is : ''', reminder)
print(f'''Divison of  {num1} and {num2} is : ''', result)

# Absolute Value
num = abs(-+7)
print("Absolute Value:", num)

# Rounding
dec = round(3.199, 1)  # Rounds to 2 decimal places
print("Rounded:", dec)