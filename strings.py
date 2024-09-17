#Escaping characters:
print('I like "Monty Python"')
print("I like \"Monty Python\"")
print("I'm Monty Python")

# Expected output:
# "I'm"
# ""learning""
# """Python"""
print("\"I'm\"","\"\"learning\"\"","\"\"\"Python\"\"\"", sep="\n")
