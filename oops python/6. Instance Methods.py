# Instance Methods are functions defined inside a class that operate on instances of the class, they can access and modify instance as well as class attributes.
# They take 'self' as the first parameter, which refers to the instance calling the method.

class Laptop:
    storage_type = "SSD"  # Class Attribute

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

        def get_info(self):
            print(f"Laptop has {self.RAM} RAM and {self.storage} storage.")

laptop1 = Laptop("16GB", "512GB")
laptop2 = Laptop("8GB", "256GB")
laptop1.get_info()  # Output: Laptop has 16GB RAM and 512GB storage.        