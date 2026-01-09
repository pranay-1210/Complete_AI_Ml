# Class is a blueprint for creating objects. An object is an instance of a class.


# Defining a class and creating an object:-

class Student:
    subject = "Maths" 
    college = "ABC College"
    year = "4th Year" 

# Creating an object of the class Student
stu1 = Student()
stu2 = Student()
print(stu1) # Output: <__main__.Student object at 0x...>
print(stu2) # Output: <__main__.Student object at 0x23e..not same as stu1>

print(stu1.subject, stu1.college, stu1.year) # Accessing attributes of the student1 object using dot notation
print(stu2.subject, stu2.college, stu2.year) # Accessing attributes of the student2 object using dot notation