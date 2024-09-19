my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_unique_list = []

for value in my_list:
    if value not in my_unique_list:
        my_unique_list.append(value)
    else:
        continue

print(my_list)
print(my_unique_list)
