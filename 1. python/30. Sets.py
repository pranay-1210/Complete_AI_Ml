# Sets are in-built data structure that stores a collection of unique elements and are mutable and un-ordered.

# Creating a set:-

my_set = {1, 2, 3, 4, 5}
print(my_set) # {1, 2, 3, 4, 5}
print(type(my_set)) # <class 'set'>

# Accessing elements of a set:-

my_set = {1, 2, 3, 4, 5}
print(my_set[0]) # TypeError: 'set' object is not subscriptable

# Adding elements to a set:-

my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set) # {1, 2, 3, 4, 5, 6}

# Creating an empty set:-

my_set = set()
print(my_set) # set()