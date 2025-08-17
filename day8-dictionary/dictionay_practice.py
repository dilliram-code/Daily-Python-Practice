# create dict: first method
dict1 = dict({"name": "Dilliram"})
print(type(dict1))

# empty dictionary
dict2 = dict()
print(dict2)

# empty dictionary
dict3 = {}

# create dict: second method
fruits = {
    "first": "apple",
    "second": "banana",
    "third": "cherry"
}
print(fruits)


# Accessing elements
personal_info = {
    "name": "Dilli",
    "age": 30,
    "email": "chaudharydr23@gmail.com",
    "married": False,
    "weight": 75.5,
    "city": "Kapilvastu"
}

# Access using key
print(personal_info["name"])

# Using get() method (avoids KeyError)
print(personal_info.get("age"))

# None (doesn’t crash): It will return None
print(personal_info.get("country"))

# With default value
print(personal_info.get("gender", "Male"))

# Importantly, .get() does not modify the dictionary. It only returns the default value temporarily for that operation.

print(personal_info)


# Adding and updating elements
personal_info["country"] = "Nepal"
print(personal_info)

# Update existing value
personal_info["married"] = True
print(personal_info)


# Removing elements

# remove specific key
del personal_info["age"]
print(personal_info)  # age key with its value will be gone


# Using pop() → removes and returns the value
pop_item = personal_info.pop("city")  # returns city name: Kapilvastu
print(pop_item)

# Using popitem() → removes last inserted item
print(personal_info)
last_item = personal_info.popitem()  # no need to pass anything
print(last_item)

# clear all items and make dictionary empty
personal_info = personal_info.clear()
print(personal_info)


# Iterating over dictionary

computer = {
    "brand": "Dell",
    "gen": "9th",
    "ram": 8,
    "storage": 256,
    "windows": 11,
    "dedicated_graphics": True

}
print("---------------------------------------------------------")
# keys
for key in computer:
    print(key)

# values
for values in computer.values():
    print(values)

# Both keys and values
for key, value in computer.items():
    print(f"{key}:{value}")

# common methods
print(computer.keys())
print(computer.values())
print(computer.items())

# copy dictionary
dublicated_coputer = computer.copy()
print(dublicated_coputer)

# update dictionary
computer.update({"year": 2025, "ssd_company": "nvidia"})
print(computer)


# Nested dictionary
students = {
    "101": {"Name": "Ram", "age": 25, "grade": "A+", "district": "Kathmandu"},
    "102": {"Name": "Sita", "age": 20, "grade": "A", "district": "Gulmi"}
}

# Access elements
print(students['101']['Name'])

# update nested value
students['101']['Name'] = "Dilli"
print(students)

print("---------------------------------------------------------")
# Dictionary comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubes = {n: n**3 for n in numbers}
print(cubes)

# Dictionary comprehension using filtering
natural_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squares less than 50
squares_less_than50 = {n: n**2 for n in natural_num if n**2 < 50}
print(squares_less_than50)

# even squares
even_squares = {n: n**2 for n in natural_num if (n**2) % 2 == 0}
print(even_squares)

# membership operator with dict: checks key's existence
friends = {
    "Rakesh": "Chemist",
    "Sukrit": "Physicist",
    "Kedar": "Linguist",
    "Anup": "Cricketer"
}

print("Rakesh" in friends)  # True
print("Dilli" in friends)   # False

# Merge dictionary
dict_1 = {"a": 1, "b":2, "c":3, "d":4}
dict_2 = {"e": 5, "f": 6, "g":7, "h": 8}

# method 1: update()
dict_1.update(dict_2)
print(dict_1)

# method 2: dictionary unpacking
merged_dict = {**dict_1, **dict_2}
print(merged_dict)


