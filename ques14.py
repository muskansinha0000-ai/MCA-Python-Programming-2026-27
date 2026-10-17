income = float(input("Enter your annual Income:"))

if income<= 25000:
    tax= 0
elif income <= 50000:
    tax = (income-25000)*0.05
elif income <= 100000:
    tax = (25000*0.05)+(income-50000)*0.2
elif income <= 200000:
    tax = (25000*0.05)+(50000*.2)+(income-100000)*0.5
else:
    tax = (25000*0.05)+(50000*.2)+(100000*.5)+(income-200000)*.7

print("Tax Payable:",tax)