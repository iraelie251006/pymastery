def add_student(students):
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student ID already exists. Please try again.")
        return
    else:
        name = input("Enter Student Name: ")
        score = float(input("Enter Student score (0-100): "))
        if score < 0 or score > 100:
            print("Invalid score. Please enter a score between 0 and 100.")
            return
        newStudent = {"name": name, "score": score}
        students[student_id] = newStudent
        print(f"Student {name} added successfully.")
        print("")

def view_all_students(students):
    if not students:
        print("No students found in the system.")
        return
    else:
        print("List of all students:")
        print("ID -- Name -- Score")
        print("----------------------")
        for student_id, student_info in students.items():
            print(f"ID: {student_id}, Name: {student_info['name']}, Score: {student_info['score']}")
        print("")

def view_student(students):
    if not students:
        print("No students found in the system.")
        return
    else:
        student_id = input("Enter Student ID to view: ")

        if student_id in students:
            student_info = students[student_id]
            print(f"ID: {student_id}, Name: {student_info['name']}, Score: {student_info['score']}")

def delete_student(students):
    if not students:
        print("No students found in the system")
        return
    else:
        student_id = input("Enter Student ID to delete: ")
        if student_id in students:
            del students[student_id]
            print("Student deleted successfully.")
        else:
            print("Student ID not found. Please try again.")

def student_performance(students):
    student_id = input("Enter Student ID to view performance: ")

    if not students:
        print("No students found in the system.")
        return
    else:
        if student_id in students:
            student_info = students[student_id]
            score = student_info['score']
            if score >= 90:
                performance = "Excellent"
            elif score >= 75:
                performance = "Good"
            elif score >= 50:
                performance = "Average"
            else:
                performance = "Poor"
            print(f"Student ID: {student_id}, Name: {student_info['name']}, Score: {score}, Performance: {performance}")
        else:
            print("Student ID not found. Please try again.")
def main():
    print("Welcome to the Student Management System")
    students = {}

    while True:
        print("1. Add Student")
        print("2. View All students")
        print("3. View specific student")
        print("4. Delete Student")
        print("5. View Student Performance")
        print("6. Exit")

        choice = input("--- Enter your choice (1-6): ")

        
        if choice == "6":
            print("Exiting the system. Goodbye!")
            break
        elif choice == "1":
            add_student(students)
        elif choice == "2":
            view_all_students(students)
        elif choice == "3":
            view_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            student_performance(students)
        print("")

if __name__ == "__main__":
    main()