PIN = int(input("Enter your pin"))
Balance = int(input("Enteryour account balance:"))
Amount = int(input("Enter Withdrawl amount:"))

if PIN == 12345:
    if Amount<=0:
        print("Invalid Amount")
    elif Amount > Balance:
        print("Insufficient Balance:")
    else:
        Balance = Balance - Amount
        print("Transaction Successful")
        print("Remaining Balance", Balance)

else:
    print("Inavlin PIN")