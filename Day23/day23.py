
"""

Lists in Python are implemented as dynamic mutable arrays which hold an ordered collection of items.

First, in many programming languages, arrays are data structures that contain a collection of elements of the same data types (for instance, all elements are integers). However, in Python, lists can contain heterogeneous data types and objects. For instance, integers, strings, and even functions can be stored within the same list. Different elements of a list can be accessed by integer indices where the first element of a list has the index of 0. This property derives from the fact that in Python, lists are ordered, which means they retain the order in which you insert the elements into the list.

Next, we can arbitrarily add, remove, and change elements in the list. For instance, the .append() method adds a new element to a list, and the .remove() method removes an element from a list. Furthermore, by accessing a list's element by index, we can change it to another element. For more detail on different list methods, please refer to the documentation.

Finally, when creating a list, we do not have to specify in advance the number of elements it will contain; therefore, it can be expanded as we wish, making it dynamic.

Lists are useful when we want to store a collection of different data types and subsequently add, remove, or perform operations on each element of the list (by looping through them). Furthermore, lists are useful to store other data structures (and even other lists) by creating, for instance, lists of dictionaries, tuples, or lists. It is very common to store a table as a list of lists (where each inner list represents a table's column) for subsequent data analysis.

Thus, the pros of lists are:

They represent the easiest way to store a collection of related objects.
They are easy to modify by removing, adding, and changing elements.
They are useful for creating nested data structures, such as a list of lists/dictionaries.
However, they also have cons:

They can be pretty slow when performing arithmetic operations on their elements. (For speed, use NumPy's arrays.)
They use more disk space because of their under-the-hood implementation.


"""

l1  = []

l2 = [1,2,'3',4]

l3  =  list()

l4 = list((1,2,3))

#printing out lists
# print(f"List l1:{l1}")
# print(f"List l2:{l2}")
# print(f"List l3:{l3}")
# print(f"List l4:{l4}")


# print(f"The  third element of the list is {l2[3]}.")
# print()


#We can also slice lists and access multiple elements simultaneously:

# l5  =  l2[2:]
# print(l5)

#appending an element to a list
l1.append(200)
# print('Appended   to the list l1:')
# 
# l1.remove(200)
# print('Removed element 200 from the list')
# print(l1)

#printing original  list l2
print("Original l2:")
print(l2)

#changing value at index 2 (third element) in l2
l2[2] = 20
# print modified  list l2
print('modified l2:')
print(l2)