print("===== SIMPLE CALCULATOR =====")
while True:
    print("\nChoose an Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponent")
    print("7. Exit")
    choice = int(input("Enter your choice (1-7): "))
    if choice == 7:
        print("Calculator Closed!")
        break
    if choice >= 1 and choice <= 6:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        if choice == 1:
            print("Result =", num1 + num2)
        elif choice == 2:
            print("Result =", num1 - num2)
        elif choice == 3:
            print("Result =", num1 * num2)
        elif choice == 4:
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Division by zero is not allowed!")
        elif choice == 5:
            if num2 != 0:
                print("Result =", num1 % num2)
            else:
                print("Modulus by zero is not allowed!")
        elif choice == 6:
            print("Result =", num1 ** num2)

    else:
        print("Invalid Choice! Please try again.")