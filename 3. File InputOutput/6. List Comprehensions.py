# List Comprehensions :- It is a new way to create lists in python using the for loop in a single line.
# It provides a concise way to generate lists by applying an expression to each item in an iterable (like a list or range) and optionally filtering items using a condition.
# The syntax for list comprehensions is: [expression for item in iterable if condition]

#Initial way for storing the squares of numbers from 0 to 9 in a list:-

squares = []

for i in range(10):
    squares.append(i*i)

print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#Using List Comprehensions to achieve the same result in a single line:-

squares_comp = [i*i for i in range(10)]
print(squares_comp)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#Example of List Comprehensions with a condition to filter even numbers and store their squares:-

even_squares = [i*i for i in range(10) if i % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]   
