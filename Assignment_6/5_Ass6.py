class Student:
    def __init__(self, roll_no, student_Name, course):
        self.roll_no = roll_no
        self.student_Name = student_Name
        self.course = course
        self.marks = {}

    def __str__(self):
        return f"Roll No: {self.roll_no}\nName: {self.student_Name}\nCourse: {self.course}\nMarks: {self.marks}"

    def accept_data(self):
        for _ in range(5):
            subject = input("Enter subject name: ")
            marks = int(input("Enter marks: "))
            self.marks[subject] = marks

    def print_data(self):
        print(self)


students = []
for _ in range(5):
    roll_no = input("Enter roll number: ")
    name = input("Enter student name: ")
    course = input("Enter course: ")
    student = Student(roll_no, name, course)
    student.accept_data()
    students.append(student)

for student in students:
    student.print_data()
