# Access Modifiers:-
# Public:- Accessible from anywhere
# Protected:- Accessible from within the class and its subclasses
# Private:- Accessible from within the class only

# Encapsulation is the concept of wrapping data and methods into a single unit, i.e., class. It restricts direct access to some of the object's components and can prevent the accidental modification of data.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

acc1 = BankAccount("123456789", 1000)
print(acc1.account_number)  # Public attribute, accessible, Output: 123456789

# Protected attribute

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute
        self._balance = balance  # Protected attribute

acc2 = BankAccount("987654321", 2000)
print(acc2._account_number)  # Protected attribute, accessible, Output: 987654321

# Private attribute

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def get_account_number(self):  # Getter method to access private attribute
        return self.__account_number

    def set_account_number(self, account_number):  # Setter method to set private attribute
        self.__account_number = account_number

acc3 = BankAccount("555555555", 3000)
print(acc3.get_account_number())  # Public method, accessible, Output: 555555555 


acc3.set_account_number("777777777")
print(acc3.get_account_number()) # Output: 777777777