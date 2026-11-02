 
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
