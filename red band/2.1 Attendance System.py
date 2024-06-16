class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.attendance_record = {}
    def mark_attendance(self, date, present= True):
        self.attendance_record[date] = present

class AttendanceSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def mark_attendance(self, date, attendance_list):
        for student, present in zip(self.students, attendance_list):
            student.mark_attendance(date, present)

    def view_attendance(self, student_name=None):
        if student_name:
            student = self.find_student(student_name)
            if student:
                print(f"Attendance for {student.name}:")
                for date, present in student.attendance_record.items():
                    print(f"{date}: {'Present' if present else 'Absent'}")
            else:
                print("Student not found.")
        else:
            print("Attendance for all students:")
            for student in self.students:
                print(f"{student.name} ({student.roll_number}):")
                for date, present in student.attendance_record.items():
                    print(f"   {date}: {'Present' if present else 'Absent'}")

    def find_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                return student
        return None

attendance_system = AttendanceSystem()

# Adding students
attendance_system.add_student(Student("Alice", 1))
attendance_system.add_student(Student("Bob", 2))

# Marking attendance
attendance_system.mark_attendance("2024-06-01", [True, False])  # Alice is present, Bob is absent
attendance_system.mark_attendance("2024-06-02", [False, True])  # Alice is absent, Bob is present

# Viewing attendance for a specific student
attendance_system.view_attendance("Alice")

# Viewing attendance for all students
attendance_system.view_attendance()
