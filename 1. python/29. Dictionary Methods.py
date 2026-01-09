# Keys Method:- Returns a list of all the keys in the dictionary

info = {
    "name": "Pranay",
    "age": 23,
    "city": "Darbhanga",
    "sub": ["Maths", "Physics", "Chemistry"]
}

print(info.keys()) # dict_keys(['name', 'age', 'city', 'sub'])

# Values Method:- Returns a list of all the values in the dictionary

info = {
    "name": "Pranay",
    "age": 23,
    "city": "Darbhanga",
    "sub": ["Maths", "Physics", "Chemistry"]
}
dict_values = info.values()
print(dict_values) # dict_values(['Pranay', 23, 'Darbhanga', ['Maths', 'Physics', 'Chemistry']])

# Items Method:- Returns a list of all the key-value pairs in the dictionary

info = {
    "name": "Pranay",
    "age": 23,
    "city": "Darbhanga",
    "sub": ["Maths", "Physics", "Chemistry"]
}

print(info.items()) # dict_items([('name', 'Pranay'), ('age', 23), ('city', 'Darbhanga'), ('sub', ['Maths', 'Physics', 'Chemistry'])])

# Clear Method:- Removes all the key-value pairs from the dictionary

info = {
    "name": "Pranay",
    "age": 23,
    "city": "Darbhanga",
    "sub": ["Maths", "Physics", "Chemistry"]
}

info.clear()
print(info) # {}

# Update Method:- Adds key-value pairs to the dictionary

info = {
    "name": "Pranay",
    "age": 23,
    "city": "Darbhanga",
    "sub": ["Maths", "Physics", "Chemistry"]
}

info.update({"name": "John"})
print(info) # {'name': 'John', 'age': 23, 'city': 'Darbhanga', 'sub': ['Maths', 'Physics', 'Chemistry']}