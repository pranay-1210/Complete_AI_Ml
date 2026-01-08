# Accessing the elements of a list:-

my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i) # 1 2 3 4 5

# Accessing the index of the elements of a list:-

my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
    print(i) # 0 1 2 3 4


# Searching a given element in a list and printing its index:-

my_list = [1, 2, 3, 4, 5]
search_element = 3
index = 0
for i in my_list:
    if i == search_element:
        print(f"search_element found at index= {index}")
        break
    index += 1

