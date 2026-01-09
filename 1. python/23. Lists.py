# Lists are a collection of items in a particular order,that are mutable.

# Creating a list:-

my_list = [1, 2, 3, 4, 5]
print(my_list)

# Accessing elements of a list:-

my_list = [1, 2, 3, 4, 5]
print(my_list[0]) # 1
print(my_list[1]) # 2
print(my_list[2]) # 3
print(my_list[3]) # 4
print(my_list[4]) # 5

print(len(my_list)) # Gives the length of the list i.e. 5

# Adding elements to a list:-

my_list = [1, 2, 3, 4, 5]
my_list[2] = "Pranay"
print(my_list) # [1, 2, 'Pranay', 4, 5]

# Slicing a list:-

my_list = [1, 2, 3, 4, 5]
print(my_list[1:3]) # [2, 3]

my_list = [1, 2, 3, 4, 5]
print(my_list[:3]) # [1, 2, 3]

my_list = [1, 2, 3, 4, 5]
print(my_list[2:]) # [3, 4, 5]

my_list = [1, 2, 3, 4, 5]
print(my_list[-1]) # 5

my_list = [1, 2, 3, 4, 5]
print(my_list[::]) # [1, 2, 3, 4, 5]