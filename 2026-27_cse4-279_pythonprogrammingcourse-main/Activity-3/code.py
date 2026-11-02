
total = int(input("Enter total number of classes: "))
attended = int(input("Enter number of classes attended: "))
required = float(input("Enter required attendance percentage: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details!")

elif required <= 0 or required > 100:
    print("Invalid eligibility percentage!")

else:
    percentage = (attended / total) * 100

    print("\n----- ATTENDANCE DETAILS -----")
    print("Total Classes:", total)
    print("Classes Attended:", attended)
    print("Current Attendance:", round(percentage, 2), "%")

    if percentage >= required:
        print("Status: Eligible")
        print("Additional Classes Required: 0")

    else:
        extra = 0

        while ((attended + extra) / (total + extra)) * 100 < required:
            extra = extra + 1

        final_percentage = ((attended + extra) / (total + extra)) * 100

        print("Status: Not Eligible")
        print("Additional Classes Required:", extra)
        print("Final Attendance:", round(final_percentage, 2), "%")
