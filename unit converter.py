while True:
    print("UNIT CONVERTER")
    print("1. Kilometer to Meter")
    print("2. Meter to Kilometer")
    print("3. Kilogram to Gram")
    print("4. Gram to Kilogram")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")
    print("7. Exit")
    choice = int(input("Enter your choice (1-7): "))
    if choice == 1:
        km = float(input("Enter distance in Kilometer: "))
        print("Meters =", km * 1000)
    elif choice == 2:
        m = float(input("Enter distance in Meter: "))
        print("Kilometers =", m / 1000)
    elif choice == 3:
        kg = float(input("Enter weight in Kilogram: "))
        print("Grams =", kg * 1000)
    elif choice == 4:
        g = float(input("Enter weight in Gram: "))
        print("Kilograms =", g / 1000)
    elif choice == 5:
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9 / 5) + 32
        print("Fahrenheit =", f)
    elif choice == 6:
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5 / 9
        print("Celsius =", c)
    elif choice == 7:
        print("Thank you for using Unit Converter!")
        break
    else:
        print("Invalid Choice! Please try again.")
