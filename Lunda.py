import os

# Global data storage
students = {}

# ========== FUNCTION DEFINITIONS ==========

def add_student():
    student_id = input("Enter Student ID: ").strip()
    if student_id in students:
        print("Student with this ID already exists.")
        return

    name = input("Enter Student Name: ").strip()
    age = int(input("Enter Student Age: "))
    grades_input = input("Enter grades separated by space: ")
    grades = [int(g) for g in grades_input.split()]

    # Store name and ID as a tuple
    info = (student_id, name)

    students[student_id] = {
        'info': info,
        'age': age,
        'grades': grades
    }

    print("Student added successfully.")

def display_students():
    if not students:
        print("No students found.")
        return

    for sid in students:
        data = students[sid]
        student_id, name = data['info']
        print(f"\nID: {student_id}, Name: {name}, Age: {data['age']}")
        print("Grades: ", end="")
        for grade in data['grades']:
            print(grade, end=" ")  # Nested loop
        print()

    # Tuple operations
    print("\n== Tuple Examples ==")
    for sid in students:
        student_id, name = students[sid]['info']
        print(f"Length of info tuple: {len((student_id, name))}")
        print(f"Max character in name: {max(name)}")
        print(f"Min character in name: {min(name)}")
        break  # show for only one student

def update_student():
    student_id = input("Enter student ID to update: ").strip()
    if student_id not in students:
        print("Student not found.")
        return

    new_name = input("Enter new name (leave blank to keep unchanged): ").strip()
    new_age = input("Enter new age (leave blank to keep unchanged): ").strip()
    new_grades_input = input("Enter new grades (space-separated, leave blank to keep unchanged): ").strip()

    if new_name:
        old_id = students[student_id]['info'][0]
        students[student_id]['info'] = (old_id, new_name)
    if new_age:
        students[student_id]['age'] = int(new_age)
    if new_grades_input:
        new_grades = [int(g) for g in new_grades_input.split()]
        students[student_id]['grades'] = new_grades

    print("Student updated.")

def delete_student():
    student_id = input("Enter student ID to delete: ").strip()
    if student_id in students:
        del students[student_id]
        print("Student deleted.")
    else:
        print("Student not found.")

def save_to_file(filename='students.txt'):
    with open(filename, 'w') as f:
        for sid, data in students.items():
            student_id, name = data['info']
            age = data['age']
            grades_str = ','.join(map(str, data['grades']))
            f.write(f"{student_id}|{name}|{age}|{grades_str}\n")
    print("Data saved to file.")

def load_from_file(filename='students.txt'):
    if not os.path.exists(filename):
        print("File not found.")
        return

    students.clear()
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split('|')
            if len(parts) != 4:
                continue  # skip malformed lines

            student_id, name, age, grades_str = parts
            grades = [int(g) for g in grades_str.split(',') if g.strip().isdigit()]

            students[student_id] = {
                'info': (student_id, name),
                'age': int(age),
                'grades': grades
            }

    print("Data loaded from file.")

def average_grades():
    for sid, data in students.items():
        grades = data['grades']
        avg = (lambda g: sum(g) / len(g) if g else 0)(grades)
        print(f"Average for {data['info'][1]}: {avg:.2f}")

def demo_lists_and_scope():
    sample_grades = [70, 80, 90]
    print("Original:", sample_grades)

    def modify_grades(grades):
        grades.append(100)  # pass by reference

    modify_grades(sample_grades)
    print("Modified:", sample_grades)

    global_var = "I am global"

    def scope_test():
        local_var = "I am local"
        print(local_var)
        print(global_var)

    scope_test()

# ========== MAIN MENU LOOP ==========

def main():
    load_from_file()

    while True:
        print("\n===== Student Information System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Show Average Grades")
        print("8. Demo Lists & Scope")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()

        if not choice.isdigit():
            print("Invalid input. Enter a number.")
            continue

        choice = int(choice)

        if choice == 1:
            add_student()
        elif choice == 2:
            display_students()
        elif choice == 3:
            update_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            save_to_file()
        elif choice == 6:
            load_from_file()
        elif choice == 7:
            average_grades()
        elif choice == 8:
            demo_lists_and_scope()
        elif choice == 9:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

# ========== RUN PROGRAM ==========

if __name__ == '__main__':
    main()