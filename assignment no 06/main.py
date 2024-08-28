def manage_student_database():
    students = []
    student_id = 1

    while True:
        name = input("Enter student name or (enter 'stop' to finish) : ")
        if name == "stop":
            break

        if name in [student[1] for student in students]:
            print("Student name already exists!")
            continue

        students.append((student_id, name))
        student_id += 1

    print("\nList of all students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")

    print("\nTotal number of students:", len(students))

    total_name_length = sum(len(student[1]) for student in students)
    print("Total length of all student names:", total_name_length)

    longest_name_student = max(students, key=lambda x: len(x[1]))
    shortest_name_student = min(students, key=lambda x: len(x[1]))
    print("Student with longest name:", longest_name_student)
    print("Student with shortest name:", shortest_name_student)

if __name__ == "__main__":
    manage_student_database()