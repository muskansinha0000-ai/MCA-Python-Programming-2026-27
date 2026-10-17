a= float(input ("Enter marks of subject a:"))
b = float(input("Enter marks of subject b:"))
c = float(input("Enter marks of subject c:"))

percentage = (a+b+c)/3
print(percentage)

if a>= 50 and b>= 60 and c>=50 and percentage >= 60:
    print("Eligible")
else:
    print("Not eligible")