#Learning about Conditional Statement IF-ELSE:

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")  


# Learning about Conditional Statement IF-ELIF-ELSE:
# ELIF and ELSE are always used with IF.

color = input("Enter a color: ")

if color == "red":
    print("Stop.")
elif color == "green":
    print("Go.")
else:
    print("Wait.")


# Various UseCases of Conditional Statements:

age = int(input("Enter your age: "))

if (age < 13):
    print("You are a child.")
elif (age >= 13 and age < 18):
    print("You are a teenager.")
else:
    print("You are an adult.")

# Checking Login Credentials:

username = input("Enter your username: ")
password = input("Enter your password: ")

if (username == "admin" and password == "password"):
    print("Access granted.")
elif (username != "admin"):
    print("Invalid username.")
else:
    print("Invalid password.")

# Checking whether a number is a multiple of 5 or not:

num = int(input("Enter a number: "))

if (num % 5 == 0):
    print("The number is a multiple of 5.")
else:
    print("The number is not a multiple of 5.")


# Checking whether a number is even or odd:

num = int(input("Enter a number: "))

if (num % 2 == 0):
    print("The number is even.")
else:
    print("The number is odd.")


# Use of Nesting Conditional Statements:

username = input("Enter your username: ")
password = input("Enter your password: ")

if (username == "admin"):
    if (password == "password"):
        print("Access granted.")
    else:
        if(password != "password"):
            print("Invalid password.")
        else:
            print("Invalid username.")
