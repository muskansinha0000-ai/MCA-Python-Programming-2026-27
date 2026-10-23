num =  int(input("Enter a number:"))

orignal = num
reverse = 0

while num > 0:
   digit = num % 10
   reverse = reverse * 10 + digit
   num = num // 10

if reverse == orignal:
   print("Palindrome ")
else:
   print("Not a Palindrome")