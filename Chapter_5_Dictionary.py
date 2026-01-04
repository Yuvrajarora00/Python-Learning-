# syntax of dictionary in Python
# dictionary is a collection of key-value pairs
# dictionaries are mutable means we can change them after creating them.
my_dict = {
    "name": "yuvraj",
    "age": 20,
    "city": "Ludhiana"
}

print(my_dict["name"])  # accessing value using key
my_dict["age"] = 21  # changing value of a key
my_dict["country"] = "India"  # adding new key-value pair
print(my_dict)

# dictionary methods
# this will return all the keys in the dictionary
print(my_dict.keys())

# this will return all the values in the dictionary
print(my_dict.values())

# this will return all the key-value pairs in the dictionary
print(my_dict.items())

# this will remove the key-value pair with key "city"
my_dict.pop("city") 
print(my_dict)

# this will clear the entire dictionary
my_dict.clear()  
print(my_dict)  

# this will update the value of key "age"
my_dict.update({"age": 22})  
print(my_dict)

# this will return the value of key "name"
print(my_dict.get("name"))

# this will add the key-value pair if key "country" does not exist
print(my_dict.setdefault("country", "India"))  

# this will create a copy of the dictionary
new_dict = my_dict.copy()
print(new_dict)

# this will remove tyhe last inserted key-value pair.
print(my_dict.popitem())  
print(my_dict)

