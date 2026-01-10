# JSON stands for JavaScript Object Notation. It is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. Python provides a built-in module called `json` to work with JSON data.

# json.loads() helps in converting a JSON string into a Python object (like a dictionary).

# json.dumps() helps in converting a Python object (like a dictionary) into a JSON string.

# json.load() helps in reading JSON data from a file and converting it into a Python object.
# json.dump() helps in writing a Python object into a file as JSON data.



import json

json_str = '{"name": "Pranay","age": 30,"city": "Darbhanga"}'

py_obj = json.loads(json_str)
print(type(py_obj), py_obj)

# Using File I/O with JSON:-

with open("../data.json", "r") as file:
    py_obj = json.load(file)
    print(type(py_obj), py_obj)  # <class 'dict'> {'name': 'Pranay', 'age': 30, 'city': 'Darbhanga', 'is_student': False, 'courses': ['Math', 'Science', 'History'], 'address': {'street': 'Laheriasarai', 'zip': '846001'}}
