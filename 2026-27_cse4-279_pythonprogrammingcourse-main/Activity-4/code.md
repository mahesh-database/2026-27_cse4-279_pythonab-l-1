# Case Study No. 26: Nested Loop Examination Seating Generator

**Student Name:** Mahesh Pedasingu  
**Roll Number:** 26000279

**Key concepts:** nested loops, two-dimensional seating layouts, reserved seats, and alternate-seat constraints.

## 1. Problem Statement

Develop a Python program to generate an examination seating arrangement using nested loops. The program should arrange students in rows and columns, assign roll numbers to available seats, keep reserved seats empty, and follow alternate seating restrictions.

The classroom has a fixed seating capacity. The program should display the final seating arrangement with row and column identifiers.

## 2. Algorithm

1. Start the program.
2. Enter the number of rows and columns.
3. Calculate the total classroom capacity.
4. Enter the number of students.
5. Check whether the number of students exceeds the classroom capacity.
6. Identify the reserved seats.
7. Use nested loops to generate rows and columns.
8. Keep reserved seats empty.
9. Apply alternate seating restrictions.
10. Assign roll numbers to available seats.
11. Display the seating arrangement.
12. Stop the program.

## 3. Flowchart
 ```mermaid

flowchart TD
    A([Start]) --> B[/Enter rows, columns and students/]
    B --> C[Calculate classroom capacity]
    C --> D{Students <= Capacity?}
    D -->|No| E[Display Capacity Error]
    E --> K([Stop])
    D -->|Yes| F[/Enter reserved seat positions/]
    F --> G[Create empty seating list]
    G --> H[Start nested loops]
    H --> I{Seat reserved?}
    I -->|Yes| J[Mark seat as R]
    I -->|No| L{Alternate restriction?}
    L -->|Yes| M[Mark seat empty]
    L -->|No| N[Assign roll number]
    J --> O[Continue to next seat]
    M --> O
    N --> O
    O --> P{All seats checked?}
    P -->|No| H
    P -->|Yes| Q[/Display seating arrangement/]
    Q --> K
```

## 4. Python Source Code

This simple program uses nested loops, lists, conditional statements, and operators.

Rules used:

- Classroom contains rows and columns.
- Reserved seats are marked as `R`.
- Alternate seating means one seat is left empty between students.
- Students are assigned roll numbers starting from 101.

```python
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
```

iframe

## 5. Sample Input

For this example, use 3 rows, 4 columns, 5 students, and 2 reserved positions.

```
Enter number of rows: 3
Enter number of columns: 4
Enter number of students: 5
Enter number of reserved seats: 2

Enter reserved seat positions (row and column):
Row: 1
Column: 2
Row: 3
Column: 4

Reserved row: 1
Reserved column: 2
Reserved row: 3
Reserved column: 4
```

## 6. Sample Output

```
EXAMINATION SEATING ARRANGEMENT

Row 1 : [101, 'R', '-', 102]
Row 2 : ['-', 103, '-', 104]
Row 3 : [105, '-', 'Empty', 'R']

Classroom Capacity: 12
Students Seated: 5
```

## 7. Additional Test Cases

| Test case | Rows | Columns | Students | Expected result      |
| --------- | ---- | ------- | -------- | -------------------- |
| 1         | 3    | 4       | 5        | Seating generated    |
| 2         | 4    | 5       | 10       | Seating generated    |
| 3         | 2    | 3       | 8        | Exceeds capacity     |
| 4         | 3    | 3       | 0        | No students assigned |
| 5         | 2    | 4       | 4        | Seating generated    |

## 8. Mermaid Flowchart Code

 <img src="https://github.com/user-attachments/assets/78c37ab9-ff3b-4873-881c-98bf9ee21a3d" />


## 9. Conclusion

The Nested Loop Examination Seating Generator helps arrange students in a classroom using rows and columns. It identifies reserved seats, follows alternate seating restrictions, and assigns roll numbers to available seats. This program demonstrates the use of nested loops, lists, conditional statements, and operators in Python.

 
