# There are several modes in which a file can be opened in Python. Here are the most commonly used modes:
# 'r'  : Read mode - Opens a file for reading. The file must exist.
# 'w'  : Write mode - Opens a file for writing. If the file exists, it truncates the file. If the file does not exist, it creates a new file.
# 'a'  : Append mode - Opens a file for appending. If the file does not exist, it creates a new file.
# 'b'  : Binary mode - Opens a file in binary mode. This is used for non-text files like images or executables.
# 't'  : Text mode - Opens a file in text mode. This is the default mode.
# '+'  : Update mode - Opens a file for both reading and writing.

# Example of opening a file in read mode
file = open("../sample.txt", "r")  # 'r' mode for reading
content = file.read()              # Read the entire content of the file
print(content)                     # Print the content to the console

file.close()                       # Closing the file

# Example of opening a file in write mode
file = open("../output.txt", "w")  # 'w' mode for writing
file.write("Hello, World!\n")      # Write a line to the file
file.close()                        # Closing the file

# Example of opening a file in append mode:-
file = open("../output.txt", "a")  # 'a' mode for appending
file.write("Appending a new line.\n")  # Append a line to the file
file.close()                        # Closing the file

# Example of opening a file in binary mode:-

file = open("../image.png", "rb")  # 'rb' mode for reading binary files
binary_content = file.read()        # Read the entire binary content of the file
print(binary_content)               # Print the binary content to the console