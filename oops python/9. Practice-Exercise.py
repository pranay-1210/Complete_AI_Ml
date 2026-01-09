'''
Design & create an online store for Products (name, price).

Track total products being created.

Create a static method to calculate discount on each product based on a % parameter.

'''

class Product:
    total_products = 0  # Class attribute to track total products
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_products += 1
        

    def get_info(self): # Instance method to display product info
        print(f"Price of {self.name} is ${self.price}")

    @classmethod
    def get_total_products(cls): # Class method to get total products
        print(f"Total products: {cls.total_products}") 

    @staticmethod
    def calculate_discount(price, discount_percent): # Static method to calculate  
        discount_amount = price * (discount_percent / 100)
        print(f"Discounted price is: ${discount_amount}")      

phone = Product("Smartphone", 699)
laptop = Product("Laptop", 999)   
tablet = Product("Tablet", 499)   

phone.get_info()  # Output: Price of Smartphone is $699

Product.get_total_products()  # Output: Total products: 3
Product.calculate_discount(999, 10)  # Output: Discounted price is: $99.9


