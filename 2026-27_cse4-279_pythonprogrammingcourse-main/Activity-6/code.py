
branches = {
    "CSE": "Computer Science Engineering",
    "ECE": "Electronics and Communication Engineering",
    "EEE": "Electrical and Electronics Engineering",
    "MEC": "Mechanical Engineering",
    "CIV": "Civil Engineering"
}

n = int(input("Enter number of students: "))

for i in range(n):

    reg = input("\nEnter registration number: ")
    reg = reg.strip().upper()

    if len(reg) == 8:

        year = reg[0:2]
        branch = reg[2:5]
        student_no = reg[5:8]

        if (year.isdigit() and
            student_no.isdigit() and
            branch in branches and
            int(year) >= 1 and
            int(student_no) >= 1):

            print("\nValid Registration Number")
            print("Admission Year: 20" + year)
            print("Branch Code:", branch)
            print("Branch Name:", branches[branch])
            print("Student Number:", student_no)

        else:
            print("Invalid Registration Number")

    else:
        print("Invalid Registration Number")

