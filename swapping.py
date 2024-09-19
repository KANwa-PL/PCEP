variable_1 = 1
variable_2 = 2

print("Variable_1: ", variable_1, "Variable_2: ", variable_2)

# Python has an easy and elegant way to swap values in a single line instead of using auxiliary variable...
variable_1, variable_2 = variable_2, variable_1

print("Variable_1: ", variable_1, "Variable_2: ", variable_2)

# The same applies to lists of values...
# It can be applied to reversing the order of values in a list.
my_list = [10, 1, 8, 3, 5]

print("My list before the swap: ", my_list)

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print("My list after the swap: ", my_list)

# And here's a 'for' loop iterating over a longer list...
my_list = [10, 1, 8, 3, 5, 23, 1, 8, 3, 5, 10, 1, 8, 3, 5, 2, 1, 8, 3, 5, 5, 1, 8, 3, 5, 33, 1, 8, 3, 5, 78, 1, 8, 3,
           5, 10, 1, 8, 3, 510, 1, 8, 3, 5, 10, 1, 8, 3, 5, 3, 1, 22, 3, 5, 3, 3, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
