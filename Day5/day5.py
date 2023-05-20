# Write a Python program to remove duplicates from a list

list1 = ['Red', 'Green','Green','White', 'White','Black','Pink', 'Black', 'Pink', 'Yellow']


# Removing Duplicates from a list

list2 = list(set(list1))
#It creates a set from the elements in list1 using the set() function. A set is an unordered collection of unique elements, meaning it removes any duplicate values from list1
# then converts the set back into a list using the list() function and assigns the result to the variable list2.


print(list2)

# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
mylist =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

mylist = [x for (i,x) in enumerate(mylist)if i not in (0,4,5)]


# mylist = [x for (i, x) in enumerate(mylist) if i not in (0, 4, 5)]
# This code iterates over the elements of the mylist and selects only those elements for which the index (i) is not in the tuple (0, 4, 5). Here's a step-by-step explanation:

# enumerate(mylist) adds an index (i) to each element (x) of mylist. This allows us to keep track of the indices while iterating.

# (i, x) represents a tuple where i is the index and x is the corresponding element from mylist.

#The condition if i not in (0, 4, 5) checks if the index i is not present in the tuple (0, 4, 5). If the index is not one of those values, the element x is selected.

#The selected elements are then collected into a new list, which is assigned back to mylist.

print(mylist)



# Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.


# num = 40
#declaring nunbers in a list
num = int(input("enter a number:"))

if num == 1:
    print(num,"is not a prime number")

elif num > 1:
    # checking the factors
    for i in range(2,num):
        if (num % i) ==0:
            print(num,"is not a prime number")
            print(i,"times",num//i, "is",num)
            break
    else:
        print(num,"is a prime number")

# if input  number is less than or
# equal to 1 , it is not a prime
else:
    print(num,"is not a prime number")
  #In summary, the code executes the specified code block for each value of i in the range from 2 to num - 1. The loop allows you to repeat a set of instructions multiple times, with i taking on different values in each iteration.



