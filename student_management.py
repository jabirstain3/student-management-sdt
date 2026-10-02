class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(self, Student):
        try:
            self.student_list.append(Student)
            print('Student added successfully.')
        except Exception as e:
            print(f'Error adding student: {e}')

        
class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

        StudentDatabase.add_student(self)

    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f"Student {self.__name} has been enrolled.")
        else:
            print(f"Student {self.__name} is already enrolled.")

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f"Student {self.__name} has been dropped.")
        else:
            print(f"Student {self.__name} is not enrolled.")

    def view_student_info(self):
        print(f"Student ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        print(f"Enrollment status: {'Yes' if self.__is_enrolled else 'No'}")


student1 = Student(101, "Jabir", "CSE", True)
student2 = Student(102, "Rahim", "EEE", False)
student3 = Student(103, "Deena", "BBA", True)

def find_student_by_id(student_id):
    for student in StudentDatabase.student_list:
        if student._Student__student_id == student_id:
            return student
    return None


while True:
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    action = input("Enter your choice (1-4): ")

    if action == "1":
        students = len(StudentDatabase.student_list)
        if students == 0:
            print("No students found.")     
        else:
            print(f"Total students: {students}")
            for student in StudentDatabase.student_list:
                student.view_student_info()
                print("--------------------")
    elif action == "2":
        try:
            student_id = int(input("Enter student ID to enroll: "))
            student_found = find_student_by_id(student_id)

            if student_found:
                student_found.enroll_student()
            else:
                print('Error: Invalid Student ID.')
    
        except ValueError:
            print("Error: Invalid input. Please enter a valid student ID.")
    
    elif action == "3":
        try:
            student_id = int(input("Enter student ID to drop: "))
            student_found = find_student_by_id(student_id)

            if student_found:
                student_found.drop_student()
            else:
                print('Error: Invalid Student ID.')

        except ValueError:
            print("Error: Invalid input. Please enter a valid student ID.")

    elif action == "4":
        print("Exiting the program.")
        break

    else:
        print("Error: Invalid choice. Please select 1-4.")

