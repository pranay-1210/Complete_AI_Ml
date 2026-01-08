# String Formatting using format function:-

name = "Pranay"
age = 23

print("My name is {} and I am {} years old.".format(name, age)) #curly braces are used to specify the position of the arguments.

# Another example:-

a = 10
b = 20
sum = a + b

print("The sum of {} and {} is {}.".format(a, b, sum))

# Index based string formatting:-

a = 10
b = 20
sum = a + b

print("The sum of {1} and {0} is {2}.".format(a, b, sum))

# Value Based Formatting:-


print("Value of vars {a} and {b}".format(a = 10, b = 20))


# Using f-string:- f-string is a new way to format strings in Python 3.6 and later versions,that is more readable and easy to use.
#It uses the f before the string to indicate that it is a formatted string.

name = "Pranay"
age = 23

print(f"My name is {name} and I am {age} years old.")

# Another example:-

a = 10
b = 20
sum = a + b

print(f"The sum of {a} and {b} is {sum}.")