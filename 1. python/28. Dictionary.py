# Dictionary are in-built data structure that stores a collection of key value pairs and are mutable and un-ordered,in which the keys are unique.

# Creating a dictionary:-

info = {
    "name": "Pranay",
    "age": 23,
    "city": "Darbhanga",
    "sub": ["Maths", "Physics", "Chemistry"]
}

print(info) # {'name': 'Pranay', 'age': 23, 'city': 'Darbhanga', 'sub': ['Maths', 'Physics', 'Chemistry']}
print(type(info)) # <class 'dict'>

# Accessing values in a dictionary:-

info = {
    "name": "Pranay",
    "age": 23,
    "city": "Darbhanga",
    "sub": ["Maths", "Physics", "Chemistry"]
}

print(info["name"]) # Pranay
print(info["age"]) # 23
print(info["sub"]) # ['Maths', 'Physics', 'Chemistry']
print(info["sub"][1]) # Physics


