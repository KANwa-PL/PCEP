# Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1.
# We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.
# Hint: the most important part of the problem is how to transform Collatz's idea into a while loop - this is the key to success.

# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, skip to point 2.

c0 = int(input("Enter non-negative and non-sero integer number... "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
    else:
        c0 = 3 * c0 + 1
    steps += 1
    print(int(c0))

print("steps = ", steps)
