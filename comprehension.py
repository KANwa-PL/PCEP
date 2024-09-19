numbers = [2, 4, 6, 7, 8, 9, 10, 12, 14, 16]
squared_uneven = [x ** 2 for x in numbers if x % 2 == 1]
squared_even = [x ** 2 for x in numbers if x % 2 == 0]
print(numbers)
print(squared_uneven)
print(squared_even)
