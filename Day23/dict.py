"""sumary_line

Dictionaries
Dictionaries in Python are very similar to real-world dictionaries. These are mutable data structures that contain a collection of keys and, associated with them, values. This structure makes them very similar to word-definition dictionaries. For example, the word dictionary (our key) is associated with its definition (value) in Oxford online dictionary: a book or electronic resource that gives a list of the words of a language in alphabetical order and explains what they mean, or gives a word for them in a foreign language.

Dictionaries are used to quickly access certain data associated with a unique key. Uniqueness is essential, as we need to access only certain pieces of information and not confuse it with other entries. Imagine we want to read the definition of Data Science, but a dictionary redirects us to two different pages: which one is the correct one? Note that technically we can create a dictionary with two or more identical keys, although due to the nature of dictionaries, it is not advisable.


"""

#creating dictionary with duplicate keys

# d1 = {"1":1,"1":2}
# print(d1["1"])

#empty dictionary
d1 = {}

## Create a two-element dictionary using curly brackets
d2  = {"John":{"Age":27, "Hometown":"Boston"}, "vincent":{"Age":24,"Hometown":"Nairobi"}}
#note the above dictionary has  a more complex as it's values are  dictionaries  themselves


#Create  an empty dictionary using  dict() constructor
d3  =  dict()


#Create a two-element dictionary using dict() Constructor
d4 = dict([["one",1],["two",2]])
#created a   dictionary  from  a list of lists

#printing out dictionaries
# print(f"Dictionary d1:{d1}")
# print(f"Dictionary d2: {d2}")
# print(f"Dictionary d3:{d3}")
# print(f"Dictionary d4: {d4}")

#Accessing an element in a list 
# print("vincent's personal data is:")
# print(d2['vincent'])


#Modifying dictionaries by adding  new key:value pairs to it
d2['mso'] = {"Age":20, "Hometown":"Nairobi"}

print(d2)