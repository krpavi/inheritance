# Inheritance
class Student:
    def __init__(self, student_name, student_age):
        self.student_name = student_name
        self.student_age = student_age
    def my_students(self):
        print("My student details")

class Teacher(Student):
    def __init__(self, student_name, student_age, teacher_name, teacher_subject):
        self.student_name = student_name
        self.student_age = student_age
        self.teacher_name = teacher_name
        self.teacher_subject = teacher_subject
    def my_teacher(self):
        print(f"student name: {self.student_name} and student age: {self.student_age}")
        print(f"teacher name: {self.teacher_name} and teacher subject: {self.teacher_subject}")


s = Teacher("Ali", 16,"Manoj", "Social Science")
s.my_teacher()
s.my_students()
