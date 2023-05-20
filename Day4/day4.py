# a is the list , it adds up all the numbers in the 
 #list a and takes start to be 0, so returning 
# only the sum of the numbers in the list.
# sum(a, start)
# this returns the sum of the list + start 


numbers = [200,100,200,300,400,199]

sum = (numbers)
print(sum)

#Program to find the second largest number in an  list
# assigning  values first in a list
list1 = [20,30,40,2,50,70,40]

# Removing Duplicates in the  list
list2 = list(set(list1))
#It creates a set from the elements in list1 using the set() function. A set is an unordered collection of unique elements, meaning it removes any duplicate values from list1
# then converts the set back into a list using the list() function and assigns the result to the variable list2.


# sorting the list
list2.sort()


print("The seceond largest number in list2 is :", list2[-2])


# ite a function in python that takes 3 parameters: name, age, and occupation and prints this sentence as output: "My name is {name}, I am {age} years old and I work as a {occupation}".



def myfunction(name, age,occupation):
    print(f"My name is  {name},I am {age} years old, and I worK as a {occupation}.")



myfunction("vincent", 24, "software engineer")




