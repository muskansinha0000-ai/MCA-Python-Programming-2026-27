while True:

    print("\n----- MENU -----")
    print("1. Prime")
    print("2. Palindrome")
    print("3. Armstrong")
    print("4. Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        num = int(input("Enter number: "))
        prime = True

        if num <= 1:
            prime = False
        else:
            for i in range(2, num):
                if num % i == 0:
                    prime = False
                    break

        if prime:
            print("Prime Number")
        else:
            print("Not a Prime Number")

    elif choice == 2:

        num = int(input("Enter number: "))
        original = num
        reverse = 0

        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10

        if original == reverse:
            print("Palindrome Number")
        else:
            print("Not a Palindrome Number")

    elif choice == 3:

        num = int(input("Enter number: "))

        original = num
        temp = num
        digits = 0

        while temp > 0:
            digits += 1
            temp //= 10

        temp = num
        total = 0

        while temp > 0:
            digit = temp % 10
            total += digit ** digits
            temp //= 10

        if total == original:
            print("Armstrong Number")
        else:
            print("Not an Armstrong Number")

    elif choice == 4:

        num = int(input("Enter number: "))
        factorial = 1

        for i in range(1, num + 1):
            factorial *= i

        print("Factorial =", factorial)

    elif choice == 5:

        n = int(input("Enter number of terms: "))

        a = 0
        b = 1

        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b

        print()

    elif choice == 6:

        print("Program Exited")
        break

    else:
        print("Invalid Choice")