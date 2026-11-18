
# Q5. Command-Line Arguments

import sys

if len(sys.argv) != 4:
    print("Usage: python Q05_Command_Line_Arguments.py number1 number2 operator")

else:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    operator = sys.argv[3]

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            sys.exit()

        result = num1 / num2

    else:
        print("Invalid operator.")
        sys.exit()

    print("Result:", result)
