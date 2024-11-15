class School():
    def __init__(self, name, address, s_list, t_list, courses, classrooms):
        self.name = name
        self.address = address
        self.s_list =  s_list
        self.t_list = t_list
        self.classrooms = classrooms
        self.courses = courses

class Person():
    def __init__ (self, name, age, address):
        self.name = name
        self.address = address
        self.age = age
        

    def get_details(self):
        return f'Name: {self.name}, Address: {self.address}'


class Student(Person):
    def __init__(self,name, age, address,s_id, grades= None):
        super().__init__(name, age, address)
        self.s_id = s_id
        self.grades = grades if grades is not None else {} 

    def add_grade(self, course, grade):
        self.grades[course] = grade
    
    def get_student_detail(self):
        details = self.get_details() #inherited method
        return f"{details}, Student ID: {self.s_id}, Grades: {self.grades}"
    
student1= Student("Subodh Ghimire", 22, "Balkumari Chowk", "S123")
student1.add_grade("Math",98)
student1.add_grade("Physics", 99)
print(student1.get_student_detail())
        
# class Student:
#     def __init__(self, student_id, name, grade, courses):
#         self.student_id = student_id
#         self.name = name
#         self.grade = grade
#         self.courses = []


#     def enroll(self, course):
#         self.courses.append(course)
    
#     def display_info(self):
#         return f"student: {self.name} (ID: {self.student_id}), Grade: {self.grade}"

# class Teacher:
#     def __init__(self, teacher_id, name, subject):
#         self.teacher_id = teacher_id
#         self.name = name
#         self.subject = subject
#         self.courses = []
    
#     def assign_course(self, course):
#         self.courses.append(course)

#     def display_info(self):
#         return f"Teacher: {self.name} (ID: {self.teacher_id}, Subject: {self.subject}"
    
# class Course:
#     def _init__(self, course_id, name, teacher):
#         self.course_id = course_id
#         self.name= name
#         self.teacher = teacher
#         self.students = []
#         teacher.assign_course(self)
    
#     def add_student(self, student):
#         self.students.append(student)
#         student.enroll(self)
#     def display_info(self):
#         return f"Course: {self.name} (ID: {self.course_id}, Teacher: {self.teacher.name})"

# if __name__ == "__main__":
#     #create teacher
#     math_teacher = Teacher("T001", "Mr. Smith", "Mathematics")
#     science_teacher = Teacher("T002", "Mrs. Johnson", "Science")

#     #Create courses
#     # 
    
#     science_course = Course("C002", "Physics", science_teacher)
#     student1 = Student("S", "jj", 10)
#     student2 = Student("S002", "Jane Smith", 10)
    
#     # Enroll students in courses
#     math_course.add_student(student1)
#     math_course.add_student(student2)
#     science_course.add_student(student1)
    
#     # Display information
#     print(student1.display_info())
#     print(math_teacher.display_info())
#     print(math_course.display_info())
#     print(f"Students in Math: {[student.name for student in math_course.students]}")