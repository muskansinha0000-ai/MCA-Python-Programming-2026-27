n = int(input("Enter an integer:"))

count = 0
for i in range(1,n+1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print("Prime number")
else:
    ("Not a Prime number")


        