
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter a number: "))

fact = factorial(num)

print("Factorial:", fact)

terms = int(input("Enter number of Fibonacci terms: "))

print("Fibonacci Series:")

for i in range(terms):
    print(fibonacci(i), end=" ")
