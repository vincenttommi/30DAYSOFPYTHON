# Sets in python

"""

In this approach, we will use a set to keep track of the elements we have seen so far. For each element in the list,
 we will check if its complement (i.e., 
 the difference between the given sum and the current element) is present in the set.
 If yes, we will add the pair to the result.


"""

"""
Algorithm
1. Initialize an empty list “result”.
2. Iterate through each element in the list “lst” and for each element, iterate through the remaining elements in the list.
3. If the sum of the two elements is equal to the given sum “K”, append the tuple of the two elements to the “result” list.
4. Return the “result” list.
"""

list = [1,5,3,7,9]

K = 12
result = []
seen = set()

for num in  list:
    complement = K - num
    if complement in seen:
        result.append((num, complement))
    seen.add(num)

print(result)        


"""

The time complexity of this algorithm is O(n), where n is the length of the given list. 
This is because we iterate over each element in the list 
once and perform constant time operations (such as set lookup and list append) for each element.

"""


# Write a Python program to return a new set with unique items from both sets by removing duplicates
def get_unique_items(set1, set2):
    unique_set = set1.union(set2)
    return unique_set


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
unique_items = get_unique_items(set1, set2)
print(unique_items)




"""



Update the first set with items that don’t exist in the second set
Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.



"""    



def update_sets(set1,set2):
    set1.difference_update(set2)


set1 = {10, 20, 30}
set2 = {20, 40, 50}

update_sets(set1,set2)

print(set1)




