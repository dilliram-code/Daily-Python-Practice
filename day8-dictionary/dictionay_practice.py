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
pop_item = personal_info.pop("city") # returns city name: Kapilvastu
print(pop_item)

# Using popitem() → removes last inserted item
print(personal_info)
last_item = personal_info.popitem()  # no need to pass anything
print(last_item)

# clear all items and make dictionary empty
personal_info = personal_info.clear()
print(personal_info)
