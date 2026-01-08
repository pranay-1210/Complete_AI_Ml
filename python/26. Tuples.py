# Tuples are immutable sequences of elements that cannot be changed once created,they are created using parentheses.

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple) # (1, 2, 3, 4, 5)
print(type(my_tuple)) # <class 'tuple'>
print(len(my_tuple)) # 5

# Tuples can also store different data types:-

my_tuple = (1, "Pranay", 3.14, True)
print(my_tuple) # (1, 'Pranay', 3.14, True)
print(type(my_tuple)) # <class 'tuple'>
print(len(my_tuple)) # 4

my_tuple = (1, 2, 3, 4, 5)
my_tuple[0] = 10 # TypeError: 'tuple' object does not support item assignment


# We can create a single element tuple by using a comma:-

my_tuple = (1)
print(type(my_tuple)) # <class 'int'>
my_tuple = (1,)
print(type(my_tuple)) # <class 'tuple'>

# Slicing a tuple:-

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4]) # (2, 3, 4)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:]) # (2, 3, 4, 5)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[:4]) # (1, 2, 3, 4)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[:]) # (1, 2, 3, 4, 5)
