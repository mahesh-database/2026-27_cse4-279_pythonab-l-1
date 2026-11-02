
# Step 1: Display the days of the week
print("Weekdays: 0-Sunday, 1-Monday, 2-Tuesday,")
print("          3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday")

# Step 2: Read input from the user
weekday = int(input("Enter starting weekday (0-6): "))
days = int(input("Enter number of days in month: "))

# Step 3: Validate the input
if weekday < 0 or weekday > 6:
    print("Invalid starting weekday!")

elif days not in [28, 29, 30, 31]:
    print("Invalid number of days in month!")

else:
    # Step 4: Print the calendar heading
    print("\n       MONTHLY CALENDAR")
    print("Sun Mon Tue Wed Thu Fri Sat")

    date = 1

    # Step 5: Generate the calendar using nested loops
    for week in range(6):

        for day in range(7):

            # Print blank spaces before the first date
            if week == 0 and day < weekday:
                print("    ", end="")

            # Print dates until the month ends
            elif date <= days:
                print(f"{date:3d} ", end="")
                date += 1

            else:
                print("    ", end="")

        # Move to the next line after Saturday
        print()

        # Stop when all dates are printed
        if date > days:
            break
