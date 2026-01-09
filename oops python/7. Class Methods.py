# Class methods are methods that are bound to the class ,cls is the first parameter of a class method and it refers to the class itself rather than an instance of the class.

class Laptop:
    storage_type = "SSD"  # Class Attribute

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod # Decorator to define a class method
    def get_storage_type(cls):
        print(f"Laptops use {cls.storage_type} storage.")

laptop1 = Laptop("16GB", "512GB")        
laptop1.get_storage_type()  # Output: Laptops use SSD storage.