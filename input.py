# Testing TypeError message.

anything = int(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.
# The results have to be printed to the console.
# You may not be able to protect the code from a user who wants to divide by zero. That's okay, don't worry about it for now.
# Test your code - does it produce the results you expect?
# We won't show you any test data - that would be too simple.

# input a float value for variable a here
a = float(input("Insert float value..."))
# input a float value for variable b here
b = float(input("Insert another float value..."))

# output the result of addition here
print("Addition " + str(a + b))
# output the result of subtraction here
print("Subtraction " + str(a - b))
# output the result of multiplication here
print("Multiplication " + str(a * b))
# output the result of division here
print("Division " + str(a / b))

x = 1
print(1 / (x + (1 / (x + (1 / (x + 1 / x))))))
x = 10
print(1 / (x + (1 / (x + (1 / (x + 1 / x))))))

x = 100
print(1 / (x + (1 / (x + (1 / (x + 1 / x))))))

x = -5
print(1 / (x + (1 / (x + (1 / (x + 1 / x))))))
