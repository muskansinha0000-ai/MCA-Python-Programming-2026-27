num = int(input("Enter a number:"))
orignal = num
sum = 0

digit = len(str(num))
while num >0:
    rem = num % 10
    sum = sum + (rem**digit)
    num = num // 10

if sum == orignal:
    print("Armstrong number")
else:
    print("Its not an Armstrong Number")