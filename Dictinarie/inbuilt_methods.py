data_pic={
        "name":"harikrishna",
        "surname":"karanam",
        "dob":"11-08-1982",
        "study":"mtech"
}
data=data_pic.copy()
print(f"{data}")

original_dict = {"a": 1, "b": 2, "c": 3}

# Using the copy() method
copied_dict_1 = original_dict.copy()

# Using the dict() constructor
copied_dict_2 = (original_dict)

print(f"Original dictionary: {original_dict}")
print(f"Copied dictionary (using copy()): {copied_dict_1}")
print(f"Copied dictionary (using dict()): {copied_dict_2}")