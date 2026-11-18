
n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    value = int(input("Enter number: "))
    numbers.append(value)

print("Original List:", numbers)

# Insert element
element = int(input("Enter element to insert: "))
position = int(input("Enter position: "))

numbers.insert(position, element)

print("After insertion:", numbers)

# Remove element
remove_element = int(input("Enter element to remove: "))

if remove_element in numbers:
    numbers.remove(remove_element)

print("After removal:", numbers)

# Sorting
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Ascending Order:", ascending)
print("Descending Order:", descending)

# Maximum, Minimum and Sum
if len(numbers) > 0:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    print("Sum:", sum(numbers))

# List concatenation
list1 = [10, 20, 30]
list2 = [40, 50, 60]

print("Concatenation:", list1 + list2)

# List repetition
print("Repetition:", list1 * 2)

# Indexing
if len(numbers) > 0:
    print("First Element:", numbers[0])

# Membership
print("20 in list:", 20 in numbers)

# List comprehension
even_numbers = [x for x in numbers if x % 2 == 0]

odd_numbers = [x for x in numbers if x % 2 != 0]

squares = [x * x for x in numbers]

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
print("Squares:", squares)

# List methods
numbers.append(100)

numbers.extend([200, 300])

numbers.insert(0, 500)

if 100 in numbers:
    numbers.remove(100)

if len(numbers) > 0:
    numbers.pop()

numbers.sort()

numbers.reverse()
