# Class Attributes are variables that are shared across all instances of a class.
# Instance Attributes are variables that are unique to each instance of a class.
# When these two attributes have the same name, the instance attribute takes precedence over the class attribute.

class Student:
    college = "ABC College"  # Class Attribute

    def __init__(self, subject, cgpa):
        self.subject = subject  # Instance Attribute
        self.cgpa = cgpa      

stu1 = Student("Maths", 9.1)
print(Student.college) # Accessing Class Attribute: Output: ABC College
print(stu1.subject)  # Accessing Instance Attribute: Output: Maths
