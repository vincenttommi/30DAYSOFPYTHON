#  Write a Python program to combine two dictionary by adding values for common keys.

dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}



# creating another variable that 
dict = {i: dict1.get(i,0) + dict2.get(i,0)
        
        for i in set(dict1).union(dict2)}

# In summary, the code merges the values of dict1 and dict2 based on their keys,
#  creating a new dictionary dict that contains the combined values.
#  If a key is missing in either dictionary, it assumes the missing value
        #printing the result

print(dict)

# Write a Python program to create a dictionary from a string.
import json
string = '{"key1": "vincent", "age": 24, "occupation": "web-dev"}'

dictionary = json.loads(string)

print(dictionary)


#Write a Python program to sort Counter by value.

