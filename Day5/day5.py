# Write a Python program to remove duplicates from a list

list1 = ['Red', 'Green','Green','White', 'White','Black','Pink', 'Black', 'Pink', 'Yellow']


# Removing Duplicates from a list

list2 = list(set(list1))
#It creates a set from the elements in list1 using the set() function. A set is an unordered collection of unique elements, meaning it removes any duplicate values from list1
# then converts the set back into a list using the list() function and assigns the result to the variable list2.


print(list2)