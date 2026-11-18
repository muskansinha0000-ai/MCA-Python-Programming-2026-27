
full_name = input("Enter full name: ")
email = input("Enter email address: ")
mobile = input("Enter mobile number: ")

# Remove extra spaces
full_name = full_name.strip()

# Extract first name and last name
name_parts = full_name.split()

first_name = name_parts[0]
last_name = name_parts[-1]

print("First Name:", first_name)
print("Last Name:", last_name)

# Reverse name using slicing
print("Reversed Name:", full_name[::-1])

# Extract username and domain
email_parts = email.split("@")

username = email_parts[0]
domain = email_parts[1]

print("Username:", username)
print("Domain:", domain)

# Extract last four digits
print("Last Four Digits:", mobile[-4:])

# Positive and negative indexing
print("First Character:", full_name[0])
print("Last Character:", full_name[-1])

# F-string formatting
print(f"Student Name: {full_name}")
print(f"Email Address: {email}")
print(f"Mobile Number: {mobile}")

# Format method
print("Student Name: {}".format(full_name))

# Percent formatting
print("Student Email: %s" % email)
