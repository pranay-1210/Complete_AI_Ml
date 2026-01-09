# Types of Inheritance in Python:-

# Single Inheritance:- In single inheritance, a class inherits from one parent class.
# Multiple Inheritance:- In multiple inheritance, a class inherits from more than one parent class.
# Multilevel Inheritance:- In multilevel inheritance, a class inherits from a child class, which in turn inherits from another parent class.
# Hierarchical Inheritance:- In hierarchical inheritance, multiple classes inherit from a single parent class.



# This is an example of Multilevel Inheritance where Accountant inherits from Administrator which in turn inherits from Employee.


class Employee:
    start_time = "9 AM"
    end_time = "5 PM"

class Administrator(Employee): 
    
    def __init__(self, department):
        self.department = department

class Accountant(Administrator): 
    
    def __init__(self, salary, department):
        super().__init__(department) # super keyword is used to call parent class (Administrator) constructor
        self.salary = salary 

acc1 = Accountant(50000, "Finance")
print(acc1.salary, acc1.department, acc1.start_time, acc1.end_time)  # Output: 50000 Finance 9 AM 5 PM             


# Example of Multiple Inheritance:-

class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa        

class TeachingAssistant(Teacher, Student):  # TeachingAssistant inherits from both Teacher and Student
    def __init__(self, salary, gpa, name):
        super().__init__(salary)  # Call Teacher's constructor
        Student.__init__(self, gpa)  # Call Student's constructor
        self.name = name

ta1 = TeachingAssistant(40000, 8.3, "Alice")
print(ta1.name, ta1.salary, ta1.gpa)  # Output: Alice 40000 8.3