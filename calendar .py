import calendar
print("CALENDAR")
year = int(input("Enter Year (e.g., 2026): "))
month = int(input("Enter Month (1-12): "))
if 1 <= month <= 12:
    print("\nCalendar:\n")
    print(calendar.month(year, month))
else:
    print("Invalid Month! Please enter a month between 1 and 12.")
