
# Global variable
x = 100


def demonstrate_scope():
    global x

    # Local variable
    y = 50

    print("Global variable:", x)
    print("Local variable:", y)

    x = 200


demonstrate_scope()

print("Updated global variable:", x)


# Lambda functions
square = lambda n: n * n

cube = lambda n: n * n * n

maximum = lambda a, b: a if a > b else b

addition = lambda a, b: a + b


print("Square:", square(5))
print("Cube:", cube(3))
print("Maximum:", maximum(10, 20))
print("Addition:", addition(10, 5))
