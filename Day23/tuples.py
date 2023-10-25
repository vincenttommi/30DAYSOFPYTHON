"""s



Tuples are almost identical to lists, 
so they contain an ordered collection of elements, 
except for one property: they are immutable. 
We would use tuples if we needed a data structure that, 
once created, cannot be modified anymore. Furthermore, 
tuples can be used as dictionary keys if all the elements are immutable.

pros of tuples
1 immutable once created cannot be changed
2 Can be used as dictionary keys if all their elements are immutable


cons of tuples
1 Tuples cannot be copied
2 They occupy more memory than lists
we cannnot use them when we want to work with modifiable objects

"""
#examples of tuples
t1 = (1,2,3,4,5)


#creating a tuple from a list tuple()constructor
t2 = tuple([1,2,3,4,5,6])


#create a tuple using  tuple constructor()
t3 = tuple([1,2,3,4,5,6,7])


#printing out tuples
# print(f"Tuple t1:{t1}") 
# print(f"Tuple t2:{t2}")
# print(f"Tuple t3:{t3}")
# t1[0] = 1
# print(t1)\

# prnting aout value at index 1  in the tuple2
# print(f"The value at index 1 in t2 is{t1[1]}")

#using tuples as dictionaries
working_hours = {("Rebecca",1):38,("Thomas",2):40}
print(working_hours)



"""


Conclusions
Let's wrap up what we have learned from this tutorial:

Data structure is a fundamental concept in programming, which is required for easily storing and retrieving data.
Python has four main data structures split between mutable (lists, dictionaries, and sets) and immutable (tuples) types.
Lists are useful to hold a heterogeneous collection of related objects.
We need dictionaries whenever we need to link a key to a value and to quickly access some data by a key, like in a real-world dictionary.
Sets allow us to perform operations, such as intersection or difference, on them; thus, they are useful for comparing two sets of data.
Tuples are similar to lists, but are immutable; they can be used as data containers that we do not want to modify by mistake.

"""

