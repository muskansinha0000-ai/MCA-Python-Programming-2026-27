
# Creating employee dictionary
employees = {
    101: {
        "name": "Rahul",
        "department": "IT",
        "salary": 35000
    },
    102: {
        "name": "Priya",
        "department": "HR",
        "salary": 40000
    },
    103: {
        "name": "Amit",
        "department": "Finance",
        "salary": 30000
    }
}

# Adding employee information
employees[104] = {
    "name": "Neha",
    "department": "Marketing",
    "salary": 45000
}

# Updating employee information
employees[101]["salary"] = 38000

# Deleting employee information
del employees[103]

# Display dictionary keys
print("Employee IDs:", employees.keys())

# Display dictionary values
print("Employee Details:", employees.values())

# Display key-value pairs
print("Employee Records:", employees.items())

# Searching employee using ID
search_id = int(input("Enter Employee ID to search: "))

if search_id in employees:
    print("Employee Found:", employees[search_id])
else:
    print("Employee Not Found")

# Dictionary comprehension
salary_limit = int(input("Enter salary limit: "))

high_salary_employees = {
    emp_id: details
    for emp_id, details in employees.items()
    if details["salary"] > salary_limit
}

print("Employees earning above specified salary:")
print(high_salary_employees)
