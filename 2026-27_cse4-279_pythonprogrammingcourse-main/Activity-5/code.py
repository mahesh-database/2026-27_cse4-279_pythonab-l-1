
name = input("Enter student name: ")

n = int(input("Enter number of questions: "))

answer_key = []
student_answers = []

print("\nEnter correct answers:")

for i in range(n):
    ans = input(f"Question {i+1}: ")
    answer_key.append(ans.strip().upper())

print("\nEnter student answers (Press Enter to skip):")

for i in range(n):
    ans = input(f"Question {i+1}: ")
    student_answers.append(ans.strip().upper())

correct = 0
incorrect = 0
unanswered = 0

for i in range(n):

    if student_answers[i] == "":
        unanswered += 1

    elif student_answers[i] == answer_key[i]:
        correct += 1

    else:
        incorrect += 1

score = (correct * 1) - (incorrect * 0.25)

print("\n----- EXAMINATION RESULT -----")
print("Student Name:", name)
print("Total Questions:", n)
print("Correct Answers:", correct)
print("Incorrect Answers:", incorrect)
print("Unanswered Questions:", unanswered)
print("Negative Marks:", incorrect * 0.25)
print("Final Score:", score)

