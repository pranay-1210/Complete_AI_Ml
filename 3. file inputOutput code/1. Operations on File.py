# File Operations in Python - Opening, Reading and Closing:-


file = open("../sample.txt", "r")  # Opening the file in read mode
content = file.read()              # Read the entire content of the file
print(content)                     # Print the content to the console

file.close()                       # Closing the file