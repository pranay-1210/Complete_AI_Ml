# With keyword is used to wrap the file operations ensuring that the file is properly closed after its suite finishes, even if an exception is raised.


# Example of using 'with' keyword to open a file in read mode:-

with open("../sample.txt", "r") as file:  # 'r' mode for reading
    content = file.read()                  # Read the entire content of the file
    print(content)                         # Print the content to the console
    
# No need to explicitly close the file, it is automatically closed when the block is exited.