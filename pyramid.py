# Your task is to write a program which reads the number of blocks the builders have
# It outputs the height of the pyramid that can be built using these blocks.

blocks = int(input("How many bricks do you have? "))
counter = 1
height = 0
while True:
    if blocks - counter >= 0:
        height += 1
        blocks -= counter
        counter += 1
    else:
        break
print("The height of the pyramid:", height)
