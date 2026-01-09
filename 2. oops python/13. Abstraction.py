# Abstraction in Python is the process of hiding the implementation details and showing only the essential features of an object to the user.
# This is typically achieved using abstract classes and methods.
# In Python, we can use the 'abc' module to create abstract base classes.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method

class Lion(Animal):
    def make_sound(self):
        print("Roar!!")  # Implementation of the abstract method

class Cow(Animal):
    def make_sound(self):
        print("Moo!!")

lion = Lion()
lion.make_sound()  # Output: Roar!!

cow = Cow()
cow.make_sound()  # Output: Moo!!!