
# Q4. Python Standard Libraries

# 1. Math Library
import math

num = int(input("Enter a number: "))

print("\n--- Math Library ---")
print("Square Root:", math.sqrt(num))
print("Factorial:", math.factorial(num))
print("Power:", math.pow(num, 2))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.7))


# 2. Random Library
import random

numbers = [10, 20, 30, 40, 50]

print("\n--- Random Library ---")
print("Random Integer:", random.randint(1, 100))
print("Random Element:", random.choice(numbers))

random.shuffle(numbers)
print("Shuffled List:", numbers)


# 3. DateTime Library
import datetime

print("\n--- DateTime Library ---")

current_date = datetime.datetime.now()

print("Current Date and Time:", current_date)
print("Day:", current_date.day)
print("Month:", current_date.month)
print("Year:", current_date.year)

date1 = datetime.date(2026, 1, 1)
date2 = datetime.date(2026, 12, 31)

difference = date2 - date1

print("Difference Between Dates:", difference.days, "days")
