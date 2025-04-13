# Merging two dictionaries using the update() method
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)
# Output: {'a': 1, 'b': 3, 'c': 4}

# Merging dictionaries using dictionary unpacking (Python 3.9+)
dict3 = {**dict1, **dict2}
print(dict3)
# Output: {'a': 1, 'b': 3, 'c': 4}