basic = float(input("Enter Basic Salary: "))

da = basic * 0.10
hra = basic * 0.20

gross = basic + da + hra
tax = gross * 0.05
net = gross - tax

print("DA =", da)
print("HRA =", hra)
print("Gross Salary =", gross)
print("Tax Deduction =", tax)
print("Net Salary =", net)