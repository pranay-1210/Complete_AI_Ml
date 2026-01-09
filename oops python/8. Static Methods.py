# In Static Methods there is no specific first parameter like self or cls.
# They can neither access instance attributes nor class attributes directly.
# @staticmethod decorator is used to convert our normal method to static method.

class Laptop:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage


    @staticmethod
    def get_discount_price(price, discount):
        discount_amount = price * (discount / 100)
        print(f"Discounted price = {discount_amount}")

laptop1 = Laptop("16GB", "512GB")
laptop1.get_discount_price(1000, 10)  # Output: Discounted price = 100.0        