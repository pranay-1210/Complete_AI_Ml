# While Loop:-

'''

 while True:
    print("Hello World")  Infinite Loop


'''


# Using a counter variable(Finite Loop):-

i = 1 #iterator
while i <= 10:
    print("Hello World") # Hello World will be printed 10 times
    i += 1 # i = i + 1

# Program to print a number in reverse order:-

i = 10
while i >= 1:
    print(i)
    i -= 1

# Print Multiplication Table of any number:-

num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "*", i, "=", num * i)
    i += 1

# Use of Break:-

i = 1
while (i <= 10):
    if(i % 6 == 0):
        break
    print(i)
    i += 1

# Use of Continue:-

i = 1
while (i <= 10):
    if(i % 3 == 0):
        i += 1
        continue
    print(i)
    i += 1

# Printing all the odd numbers from 1 to 100:-


i = 1
while (i <= 100):
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1