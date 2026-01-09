# Default Constructor are constructors that do not take any parameters other than self. They initialize the object with default values.
# Parameterized Constructor are constructors that take parameters to initialize the object with specific values provided during object creation.

# Default Constructor:-

class Student:
    def __init__(self): # Default Constructor
        print ("Default Constructor was called...")

stu1 = Student()  # Output: Default Constructor was called...
stu2 = Student()  # Output: Default Constructor was called...

# Parameterized Constructor:-

class Student:
    def __init__(self, subject, cgpa): # Parameterized Constructor
        self.subject = subject
        self.cgpa = cgpa

stu1 = Student("Maths", 9.1)
stu2 = Student("Science", 8.5)
print(stu1.subject, stu1.cgpa) # Output: Maths 9.1
print(stu2.subject, stu2.cgpa)  # Output: Science 8.5

# NOTE : In Python, We cannot have multiple constructors like some other programming languages.