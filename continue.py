# Your program must:
# ask the user to enter a word;
# use user_word = user_word.upper() to convert the word entered by the user to upper case
# use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
# print the uneaten letters to the screen, each one of them on a separate line.

user_word = input("Enter a word... ")
user_word = user_word.upper()

for letter in user_word:
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    else:
        print(letter, end='\n')

# Your task here is even more special than before:
# You must redesign the (ugly) vowel eater from the previous lab (3.1.2.10) and create a better, upgraded (pretty) vowel eater!
# Write a program that uses:
# Assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.

user_word = input("Enter a word... ")
user_word = user_word.upper()
word_without_vowels = ''

for letter in user_word:
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels)
