
# Creating a tuple
roll_numbers = (101, 102, 103, 104, 105)

print("Tuple Elements:", roll_numbers)

# Tuple indexing
print("First Element:", roll_numbers[0])

# Tuple slicing
print("Sliced Tuple:", roll_numbers[1:4])

# Tuple concatenation
tuple1 = (101, 102, 103)
tuple2 = (104, 105, 106)

print("Concatenated Tuple:", tuple1 + tuple2)

# Creating two sets
course_a = {101, 102, 103, 104}
course_b = {103, 104, 105, 106}

# Set operations
print("Union:", course_a.union(course_b))

print("Intersection:", course_a.intersection(course_b))

print("Difference:", course_a.difference(course_b))

print("Symmetric Difference:",
      course_a.symmetric_difference(course_b))

# Subset and Superset
print("Is Subset:", course_a.issubset(course_b))

print("Is Superset:", course_a.issuperset(course_b))

# Adding an element
course_a.add(107)

# Removing an element
course_a.remove(101)

# Set comprehension
even_squares = {
    x * x for x in range(1, 11) if x % 2 == 0
}

print("Squares of Even Numbers:", even_squares)
