# Append Method:- It adds an element to the end of the list

my_list = [1, 2, 3]
my_list.append(4)
print(my_list) # [1, 2, 3, 4]

# Insert at given index:-

my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list) # [1, 4, 2, 3]

# Sort Method :- By default sorts the list in ascending order

my_list = [5, 2, 9, 4, 1]
my_list.sort()
print(my_list) # [1, 2, 4, 5, 9]

# Sort Method :- Sorting the list in descendingorder

my_list = [5, 2, 9, 4, 1]
my_list.sort(reverse = True)
print(my_list) # [9, 5, 4, 2, 1]

# Reverse Method:- Reverses the list

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list) # [5, 4, 3, 2, 1]