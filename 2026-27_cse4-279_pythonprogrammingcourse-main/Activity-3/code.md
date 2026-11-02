# Case Study No. 12: Attendance Recovery Computation

**Student Name:** Mahesh Pedasingu  
**Roll Number:** 26000279

**Key concepts:** percentage calculation, conditional logic, and estimating the classes needed to meet an attendance target.

## 1. Problem Statement

Develop a Python program to calculate the current attendance percentage of a student and determine the minimum number of consecutive classes the student must attend to reach the required attendance eligibility percentage.

The program should accept the total number of classes conducted and the number of classes attended. It should calculate the current attendance percentage and find the additional classes required to achieve the eligibility threshold under different future attendance scenarios.

## 2. Algorithm

1. Start the program.
2. Enter the total number of classes conducted.
3. Enter the number of classes attended.
4. Enter the required attendance percentage.
5. Calculate the current attendance percentage.
6. Check whether the student has already reached the required percentage.
7. If not, calculate the minimum additional consecutive classes required.
8. Display the current attendance percentage.
9. Display the number of additional classes required.
10. Display the final attendance percentage.
11. Stop the program.

## 3. Flowchart

 ```mermaid

flowchart TD
    A([Start]) --> B[/Enter total classes, attended classes and required percentage/]
    B --> C{Are inputs valid?}
    C -->|No| D[Display Invalid Input]
    D --> I([Stop])
    C -->|Yes| E[Calculate current attendance percentage]
    E --> F{Attendance >= Required percentage?}
    F -->|Yes| G[Display Eligible]
    F -->|No| H[Set extra = 0]
    H --> J{Future attendance >= Required percentage?}
    J -->|No| K[Increase extra by 1]
    K --> J
    J -->|Yes| L[Display additional classes required]
    G --> M[/Display attendance details/]
    L --> M
    M --> I
```

## 4. Python Source Code

This program uses variables, operators, conditional statements, loops, and input validation.

```python
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
```

## 5. Sample Input

```
Enter total number of classes: 100
Enter number of classes attended: 70
Enter required attendance percentage: 75
```

## 6. Sample Output

```
----- ATTENDANCE DETAILS -----
Total Classes: 100
Classes Attended: 70
Current Attendance: 70.0 %
Status: Not Eligible
Additional Classes Required: 20
Final Attendance: 75.0 %
```

## 7. Additional Test Cases

| Test case | Total classes | Attended | Required | Additional classes |
| --------- | ------------- | -------- | -------- | ------------------ |
| 1         | 100           | 70       | 75%      | 20                 |
| 2         | 100           | 80       | 75%      | 0                  |
| 3         | 50            | 30       | 75%      | 30                 |
| 4         | 80            | 60       | 75%      | 0                  |
| 5         | 100           | 60       | 75%      | 60                 |

## 8. Mermaid Flowchart Code
 <img src="<img width="1316" height="2312" alt="mermaid-diagram (3)" src="https://github.com/user-attachments/assets/ea6ad465-b0bc-403f-821e-20af856ae95c" />

## 9. Conclusion

The Attendance Recovery Computation program calculates the current attendance percentage of a student and determines the minimum number of additional consecutive classes required to achieve the eligibility percentage. It uses Python conditional statements and loops to perform calculations and display the result. This program helps students understand attendance calculations and basic Python programming concepts.


