string = "hello"

for char in string:  # in -> membership operator(To check the presence of a character in a string)
    print(char) 

#Membership operator can also be used with conditional statements:-

string = "pranay"

if "a" in string:
    print("a is present in string.")
else:
    print("a is not present in string.")


# For Loop with range function:-

for i in range(5): # range function returns a sequence of numbers from 0 to n-1
    print(i)

for i in range(1,10,2): # range(start,stop,step) means start to stop with step 1
    print(i)    


# Program to count a given character in a string:- 


word = "machine learning"

count = 0 

for char in word:
    if(char == "a"):
        count += 1

print("Count of 'a' is = ", count)


# Program to count vowels from a given string:-


word = input("Enter a word: ")

count = 0

for char in word:
    if(char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
        count += 1

print("Count of vowels is = ", count)


# Program to print the sum of first n natural numbers:-


n = int(input("Enter a number: "))

sum = 0

for i in range(1,n+1):
    sum += i

print("Sum of first", n, "natural numbers is = ", sum)