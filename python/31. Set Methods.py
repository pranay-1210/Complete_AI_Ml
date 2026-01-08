# Remove Method:- Removes the specified element from the set

my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set) # {1, 2, 4, 5}

# Clear Method:- Removes all the elements from the set

my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set) # set()

# Pop Method:- Removes and returns an arbitrary element from the set

my_set = {1, 2, 3, 4, 5}
my_set.pop()
print(my_set) # {2, 3, 4, 5}

# Union Method:- Returns a new set with all items from both sets

set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.union(set2)
print(set3) # {1, 2, 3, 4, 5, 6}

# Intersection Method:- Returns a new set with common items from both sets

set1 = {1, 2, 4}
set2 = {4, 5, 6}
set3 = set1.intersection(set2)
print(set3) # {4}