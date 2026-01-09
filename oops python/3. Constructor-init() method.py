# Constructor in Python are defined using the __init__() method, which is automatically called when an object of the class is created.
# It is used to initialize the attributes of the object.
# The __init__() method can take parameters to allow for dynamic initialization of object attributes.
# self parameter refers to the current instance of the class and is used to access variables that belong to the class.

class Student:
    def __init__(self):
        print("Constructor was called...")

stu1 = Student()  # Output: Constructor was called... 
stu2 = Student()  # Output: Constructor was called...

# Parameterized Constructor

class Student:
    def __init__(self, subject, cgpa):
        self.subject = subject
        self.cgpa = cgpa

stu1 = Student("Maths", 9.1)
stu2 = Student("Science", 8.5)

print(stu1.subject, stu1.cgpa) # Output: Maths 9.1  
print(stu2.subject, stu2.cgpa)  # Output: Science 8.5
