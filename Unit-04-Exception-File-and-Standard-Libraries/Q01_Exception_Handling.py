
# Q1. Exception Handling

# 1. Handling division by zero
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")

else:
    print("Division Result:", result)

finally:
    print("Division operation completed.")


# 2. Handling invalid list index
try:
    numbers = [10, 20, 30, 40]
    index = int(input("Enter list index: "))
    print("Element:", numbers[index])

except IndexError:
    print("Error: Invalid list index.")

except ValueError:
    print("Error: Please enter a valid index.")


# 3. Using raise to generate an exception
try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("You are eligible.")

except ValueError as e:
    print("Error:", e)
