# Inheritance is a fundamental concept in object-oriented programming that allows a class (called a child or subclass) to inherit attributes and methods from another class (called a parent or superclass). This promotes code reusability and establishes a hierarchical relationship between classes.

# Example of Inheritance:-

class Employee:
    start_time = "9 AM"
    end_time = "5 PM"

class Teacher(Employee):  # Teacher class inherits from Employee class
    
    def __init__(self, subject):
        self.subject = subject

class Administrator(Employee):  # Administrator class inherits from Employee class
    
    def __init__(self, department):
        self.department = department


t1 = Teacher("Mathematics")
print(t1.subject, t1.start_time, t1.end_time)    # Output: Mathematics 9 AM 5 PM  

a1 = Administrator("Human Resources")
print(a1.department, a1.start_time, a1.end_time)  # Output: Human Resources 9 AM 5 PM

