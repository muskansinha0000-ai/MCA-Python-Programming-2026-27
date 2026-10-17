data = float(input("Enter monthly data usage in GB:"))

if data <= 2:
    bill = 100
elif data <= 5:
    bill = 100 + (data - 2)*50
elif data <= 7:
    bill = 100 + (data -5)*70
elif data <= 9:
    bill = 100 + (data-7)*90
else:
    bill = 100 + (data-9)*99
print("Amount",bill)    
