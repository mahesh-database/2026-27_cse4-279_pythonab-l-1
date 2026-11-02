
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
students = int(input("Enter number of students: "))

capacity = rows * cols

if rows <= 0 or cols <= 0 or students < 0:
    print("Invalid input!")

elif students > capacity:
    print("Students exceed classroom capacity!")

else:
    reserved = int(input("Enter number of reserved seats: "))

    if reserved < 0 or reserved > capacity:
        print("Invalid reserved seats!")

    else:
        seating = []
        roll = 101
        reserved_count = 0

        print("Enter reserved seat positions (row and column):")

        for i in range(reserved):
            r = int(input("Row: "))
            c = int(input("Column: "))

            if 1 <= r <= rows and 1 <= c <= cols:
                reserved_count += 1
            else:
                print("Invalid position!")

        if reserved_count != reserved:
            print("Please enter valid reserved positions.")
        else:
            reserved_seats = []

            # Read reserved positions again
            for i in range(reserved):
                r = int(input("Reserved row: "))
                c = int(input("Reserved column: "))
                reserved_seats.append((r, c))

            for i in range(rows):
                row = []

                for j in range(cols):

                    if (i + 1, j + 1) in reserved_seats:
                        row.append("R")

                    elif (i + j) % 2 == 1:
                        row.append("-")

                    elif roll < 101 + students:
                        row.append(roll)
                        roll += 1

                    else:
                        row.append("Empty")

                seating.append(row)

            print("\nEXAMINATION SEATING ARRANGEMENT")

            for i in range(rows):
                print("Row", i + 1, ":", seating[i])

            print("Classroom Capacity:", capacity)
            print("Students Seated:", roll - 101)

