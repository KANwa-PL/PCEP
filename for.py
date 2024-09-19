import time

for i in range(1, 2):
    print(str(i) + " Mississippi...")
    time.sleep(1)
print("Ready or not, here I come!")

# Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
for i in range(1, 11):
    if i % 2 == 1: print(i)

# Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
x = 0
while x < 11:
    if x % 2 == 1: print(x)
    x += 1

# Create a program with a for loop and a break statement.
# The program should iterate over characters in an email address, exit the loop when it reaches the @ symbol,
# and print the part before @ on one line. Use the skeleton below:
email_address = "john.smith@pythoninstitute.org"
email_prefix = ""
for letter in email_address:
    if letter == "@":
        break
    else:
        email_prefix += letter
print(email_prefix)

# Create a program with a for loop and a continue statement.
# The program should iterate over a string of digits, replace each 0 with x,
# and print the modified string to the screen. Use the skeleton below:

modified_string = ""
for digit in "0165031806510":
    if digit == "0":
        modified_string += 'x'
        continue
    else:
        modified_string += digit
print(modified_string)
