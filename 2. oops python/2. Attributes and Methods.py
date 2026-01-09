# A Class can store attributes (data) and methods (functions) that define the behavior of the objects created from the class.

class Student:
    subject = "Maths"   # Class attribute
    college = "ABC College"
    year = "4th Year" 

    def greet(self): # Method defined within the class
        return f"Welcome to {self.college}!"
    

stu1 = Student()
print(stu1.greet())  # Output: Welcome to ABC College!