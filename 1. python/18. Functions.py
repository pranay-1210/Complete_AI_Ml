'''
Functions are a block of code that performs a specific task and returns a value. They can be used to break down complex programs into smaller, more manageable parts.

'''
def my_function():  # Defining a function
    print("Hello from a function")
    print("How are you?")

my_function()  # Calling a function    

# Function with parameters(Sum of two numbers):-



def sum(num1, num2):
    return num1 + num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

ans = sum(num1, num2)
print("The sum of", num1, "and", num2, "is", ans)