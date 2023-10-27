"""

Python - Sorting Algorithms
refers  to arranging data in a particular format

types of sorting 


1 Bubble-sort
2 Merge Sort
3 Insertio Sort
4 shell Sort
5 Selection Sort
    """
    


#1 Bubble Sort - is  a comparison based algorithm with each pair of adjacent elements are  compared 
#and if not the same they are swapped 
    
    
def bubblesort(list):
    #swapping the  elements to arrage in order
    for number in range(len(list)-1, 0,-1):
        for idx in range(number):
            if list[idx] > list[idx + 1]:
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx+1]  = temp
list = [20,34,45,67,88,90,34,56,67,23 ,2 ,20,78,19,14,13,11,10,9,89]
bubblesort(list)
print(list)                


             
             
            