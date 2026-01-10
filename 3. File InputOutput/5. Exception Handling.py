# Exception Handling in Python is a mechanism to handle errors and exceptions that occur during the execution of a program.
# It allows developers to gracefully manage unexpected situations without crashing the program.
# The primary keywords used for exception handling in Python are try, except, else and  finally.

# Example of Exception Handling using try, except and finally:-

try:
    x = int(input("Enter a number: "))
    ans = 10 / x

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

else :
    print(f"The result is: {ans}")

finally:
    print("Execution completed.")