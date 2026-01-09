# Polymorphism in Python is the ability to present the same interface for different data types.
# It allows methods to do different things based on the object it is acting upon, even though they share the same name.
# Method overriding is a common way to achieve polymorphism in object-oriented programming,in which a subclass provides a specific implementation of a method that is already defined in its superclass.


class Employee:
    def get_designation(self):
        print("designation = Employee")

class Teacher(Employee):
    def get_designation(self):  # Method overriding
        print("designation = Teacher")

t1 = Teacher()
t1.get_designation()  # Output: designation = Teacher