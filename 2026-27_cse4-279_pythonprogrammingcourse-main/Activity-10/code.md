# Case Study: Student Group Formation with Score Balancing

**Student Name:** Mahesh Pedasingu  
**Roll Number:** 26000279

**Key concepts:** sorting, nested lists, input validation, and greedy balancing of group totals.

## 1. Problem Statement

Develop a Python program to divide students into groups based on their scores. The program should accept student scores and the required size of each group. It should arrange students so that the total scores of all groups are as balanced as possible while following the specified group sizes.

## 2. Algorithm

1. Start the program.
2. Read the number of students.
3. Read the scores of all students.
4. Read the number of groups.
5. Read the required size of each group.
6. Check whether the sum of group sizes equals the total number of students.
7. Sort student scores in descending order.
8. Create empty groups with the specified sizes.
9. Assign each student to the group with the lowest total score that still has space.
10. Calculate the total score of each group.
11. Display the students and total scores in each group.
12. Stop the program.

## 3. Flowchart

 ```mermaid
flowchart TD
    A([Start]) --> B[/Enter student scores/]
    B --> C[/Enter number of groups and group sizes/]
    C --> D{Do group sizes equal student count?}
    D -- No --> E[Display error message]
    E --> K([Stop])
    D -- Yes --> F[Sort scores in descending order]
    F --> G[Create empty groups and totals]
    G --> H[Select next highest score]
    H --> I[Find group with lowest total and available space]
    I --> J[Assign student and update group total]
    J --> L{All students assigned?}
    L -- No --> H
    L -- Yes --> M[Display groups and total scores]
    M --> N[Calculate score difference]
    N --> K
```
## 4. Python Source Code

```python
 
n = int(input("Enter number of students: "))

scores = []

for i in range(n):
    score = int(input(f"Enter score of student {i + 1}: "))
    scores.append(score)

 
groups_count = int(input("Enter number of groups: "))

group_sizes = []

for i in range(groups_count):
    size = int(input(f"Enter size of group {i + 1}: "))
    group_sizes.append(size)

 
if sum(group_sizes) != n:
    print("Error: Total group sizes must equal number of students.")

elif any(size <= 0 for size in group_sizes):
    print("Error: Group sizes must be positive.")

elif any(score < 0 or score > 100 for score in scores):
    print("Error: Scores must be between 0 and 100.")

else:
    
    scores.sort(reverse=True)

    
    groups = [[] for i in range(groups_count)]
    totals = [0] * groups_count
 
    for score in scores:
        best_group = -1

        for i in range(groups_count):
            if len(groups[i]) < group_sizes[i]:
                if best_group == -1 or totals[i] < totals[best_group]:
                    best_group = i

        groups[best_group].append(score)
        totals[best_group] += score
 
    print("\nSTUDENT GROUP DETAILS")

    for i in range(groups_count):
        print(f"\nGroup {i + 1}:")
        print("Scores:", groups[i])
        print("Total Score:", totals[i])

    print("\nDifference between highest and lowest group totals:",
          max(totals) - min(totals))
```

## 5. Sample Input

```
Enter number of students: 8
Enter score of student 1: 95
Enter score of student 2: 90
Enter score of student 3: 85
Enter score of student 4: 80
Enter score of student 5: 75
Enter score of student 6: 70
Enter score of student 7: 65
Enter score of student 8: 60

Enter number of groups: 4
Enter size of group 1: 2
Enter size of group 2: 2
Enter size of group 3: 2
Enter size of group 4: 2
```

## 6. Sample Output

```
STUDENT GROUP DETAILS

Group 1:
Scores: [95, 60]
Total Score: 155

Group 2:
Scores: [90, 65]
Total Score: 155

Group 3:
Scores: [85, 70]
Total Score: 155

Group 4:
Scores: [80, 75]
Total Score: 155

Difference between highest and lowest group totals: 0
```

 



 
## 8. Conclusion

This program uses Python lists, loops, sorting, and conditional statements to divide students into balanced groups. It assigns higher scores first to the group with the lowest current total, while respecting the specified group sizes.

 
