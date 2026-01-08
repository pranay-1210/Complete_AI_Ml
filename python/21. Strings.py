# Strings are a sequence of characters

name = "Pranay"
love = "Loves Machine Learning"
sentence = name + " " + love

print(sentence)

# String Indexing:-

name = "Pranay"
print(name[0]) # P
print(name[1]) # r
print(name[2]) # a
print(name[3]) # n
print(name[4]) # a
print(name[5]) # y

# Using for loop to print all the characters of a string:-

name = "Pranay"

for char in name:
    print(char)

# String Length:-

name = "Pranay"
print(len(name))

# String Slicing:-

name = "Pranay"
print(name[0:4]) # Pran

name = "Pranay"
print(name[2:]) # anay

name = "Pranay"
print(name[:4]) # Pran

name = "Pranay"
print(name[-4:]) # anay

name = "Pranay"
print(name[::]) # Pranay