secret_number = 777

print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)

number = int(input("Enter number..."))

while number != secret_number:
    number = int(input("Ha ha! You're stuck in my loop!"))
    if number > secret_number:
        print("Try lower numbers...")
    elif number < secret_number:
        print("Try higher numbers...")
print("Well done, muggle! You are free now.")
