# Illegal variable names
TRUE = True
true = True
# and = True
# True = True

# Integer division.
x = 2
y = 4
x = x // y
# y = y // x # ZeroDivisionError: integer division or modulo by zero
print(y)

# Another division
print(1 / 1)  # 1.0
print(1 // 2 * 3)  # 0
