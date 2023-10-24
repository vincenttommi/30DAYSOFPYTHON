"""

Sets in Python can be defined as mutable dynamic collections of immutable unique elements. The elements contained in a set must be immutable. Sets may seem very similar to lists, but in reality, they are very different.

First, they may only contain unique elements, so no duplicates are allowed. Thus, sets can be used to remove duplicates from a list. Next, like sets in mathematics, they have unique operations which can be applied to them, such as set union, intersection, etc. Finally, they are very efficient in checking whether a specific element is contained in a set.

Thus, the pros of sets are:

We can perform unique (but similar) operations on them.
They are significantly faster than lists if we want to check whether a certain element is contained in a set.
But their cons are:

Sets are intrinsically unordered. If we care about keeping the insertion order, they are not our best choice.
We cannot change set elements by indexing as we can with lists.


"""


# Examples of  sets
# s1 =  {1,2,3}

# #create a set using the set constructor
# s2  = set([1,2,3,4])

# #printing out sets 

# print(f"Set s1:{s1}")
# print(f"Set s2:{s2}")


#creating an iterable set


#creating two sets
names1 = set(["Glory","Tony","Dennis","vincent","Lilian"])
names2  = set(["Morgan","joel","Emmanuel","Diego","Medrine"])

#creating a union of sets using the  | operator
# names_union  = names1 |  names2


#creating a union of sets  using  union() method 
# names_union = names1.union(names2)


#printing out the resulting union
# print(names_union)


#instersection of two set , what to knwo which sets appear  in both sets
# names_intersection = names1.intersection(names2)


#Intersectionof two sets using the & operator
names_intersection = names1 & names2


#printing  out the resulting  intersetion
print(names_intersection)
