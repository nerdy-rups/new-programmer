#illustration of using the concepts of class and methods to add imaginary students to some courses

class Student:
    def __init__(self, name, age, grade):
        self.student_name = name
        self.student_age = age
        self.student_grade = grade
    def get_grade(self):
        return (self.student_grade)

class Course:
    def __init__(self, name, max_number_allowed):
        self.course_name = name
        self.maximum_number = max_number_allowed
        self.students_enrolled = [] # like normal functions,# we can create placeholder variables inside the
        # method like this which are not passed during method call.
    def add_students(self, student):
        if len(self.students_enrolled) < self.maximum_number:
            self.students_enrolled.append(student)
            return True
        return False
    def average_grade(self):
        value = 0
        for s in self.students_enrolled: # here s actually becomes each object of Student class that get
            # stored in the students_enrolled list as per the last method
            value = value + Student.get_grade(s)
        return value/len(self.students_enrolled)

s1 = Student("Tom", 24, 60)
s2 = Student("John", 44, 30)
s3 = Student("Mary", 56, 19)
course1 = Course("Maths", 3)
course1.add_students(s1); course1.add_students(s2); course1.add_students(s3)
print("The average marks in", course1.course_name, "is", int(course1.average_grade()))

