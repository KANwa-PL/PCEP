# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.

# Not within the Gregorian calendar period
# Leap year or Common year

year = int(input("Enter a year: "))

if year <= 1582:
    print("Not within the Gregorian calendar period")
elif year % 4 != 0:
    if year % 400 != 0:
        print("Common year")
elif year % 100 != 0:
    print("Leap year")
else:
    print("Leap year")
