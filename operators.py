# Expected result = 10.0
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

# Expected result = 5.0
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

# Create the variables: john, mary, and adam containing values representing apples...
john = 5
mary = 2
adam = 7

# Print the variables on one line, and separate each of them with a comma...
print(john, mary, adam, sep=", ")

# Now create a new variable named total_apples equal to addition of the three former variables...
total_apples = john + mary + adam
print("Total apples:", total_apples)


# Bearing in mind that 1 mile is equal to approximately 1.61 kilometers, complete the program in the editor so that it converts:
# miles to kilometers
# kilometers to miles

def convert_miles_to_kilometers(miles):
    return miles * 1.61


def convert_kilometers_to_miles(kilometers):
    return kilometers / 1.61


kilometers = 12.25
miles = 7.38

print(round(convert_miles_to_kilometers(miles), 2))
print(round(convert_kilometers_to_miles(kilometers), 2))

# 3x3 - 2x2 + 3x - 1
x = 0.0
print("y =", 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1)
x = 1.0
print("y =", 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1)
x = -1.0
print("y =", 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1)
