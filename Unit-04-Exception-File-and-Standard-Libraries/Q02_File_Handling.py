
# Q2. File Handling - Read, Write and Append

# Creating and writing student details
file = open("student.txt", "w")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
course = input("Enter course: ")

file.write("Student Name: " + name + "\n")
file.write("Roll Number: " + roll_no + "\n")
file.write("Course: " + course + "\n")

file.close()

print("Student details written successfully.")


# Reading complete file contents
file = open("student.txt", "r")

print("\nComplete File Contents:")
print(file.read())

file.close()


# Appending additional student records
file = open("student.txt", "a")

name = input("\nEnter another student name: ")
roll_no = input("Enter roll number: ")
course = input("Enter course: ")

file.write("\nStudent Name: " + name + "\n")
file.write("Roll Number: " + roll_no + "\n")
file.write("Course: " + course + "\n")

file.close()

print("Additional student record added.")


# Reading file line by line
file = open("student.txt", "r")

print("\nReading File Line by Line:")

for line in file:
    print(line, end="")

file.close()

print("\nFile closed successfully.")
