#this program is how to assign a basic dictinary 
data_dict1={"Hari":"Krishma",
            "mobilenumber":9949024114,
            'surname': 'karanam'
}
print(data_dict1)
##adding new data to the dictioary
data_dict1['brother']='prudhvi'
data_dict1["son"]="Aakarsh"
print(data_dict1)
data_dict2=data_dict1.items() #will get both values and keys
print(data_dict2)
keys1=data_dict1.keys()
print(f"keys of dictionary is {keys1}")
