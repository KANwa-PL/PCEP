# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)

# Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word,
# in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.

while True:
    secret = str(input("Enter secret word..."))
    if secret == "chupacabra":
        break
print("You've successfully left the loop.")
