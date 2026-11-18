
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"


def calculate(a, b, operation="addition"):
    if operation == "addition":
        return addition(a, b)
    elif operation == "subtraction":
        return subtraction(a, b)
    elif operation == "multiplication":
        return multiplication(a, b)
    elif operation == "division":
        return division(a, b)
    else:
        return "Invalid operation"


# Positional arguments
result1 = addition(10, 5)

# Keyword arguments
result2 = subtraction(a=10, b=5)

# Default argument
result3 = calculate(10, 5)

# Specifying operation
result4 = calculate(10, 5, operation="multiplication")
