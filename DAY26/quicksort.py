#  a highly efficient sorting algorithm and is based on partitioning of array of data into smaller array
# A large array  is  partitioned into two arrays  one of which holds  values smaller  than  specified value

#QuickSort  partitions an array and then  calls itself  recursivelytwice to  sort  the two resulting
# subarrays.

#Quick Sort Pseudocode

""""sumary_line




function partionFunc(left,right,pivot)
leftPointer = left
rightPointer  =  right - 1


while  True do
  while  A[++left[pointer]<
  //do-nothing
  end while
  
  
  while rightPointer > 0 && A[--rightPointer] > pivot do
  //do-nothing
  
  if leftPointer >= rightPointer
    break
   else
    swap leftPointer, rightPointer
    
    endif
    endwhile 
    
    swap leftPointer,right
    return leftPointer
    
    
    end function
    
    
    Quick Sort  Algorithm 
    we end up with smaller  possible  partitions. Each partition is then processed for quick sort
    
    step 1 - Make the  right-most index value pivot
    step 2   - partition the array using pivot value
    step 3  - quicksort  left partition  recursively
    step 4 - quicksort  right partition recursivley
    
    
    #Quick Sort Pseudocode
    
    procedure quickSort(left, right)
    
    if right-left <= 0
      return 
    else
    pivot  = A[right]
    partition =  partitionFunc(left,right,pivot)
    quickSort(left, partiton-1)
    quickSort(partition+1, right)
    
    end if 
     
  
  ]
"""


#python program for  Quick Sort Algorithm

def printline(count):
    for i in range(count - 1):
        print("=", end="")
    print("=")

def display(arr):
    print("[", end="")
    for item in arr:
        print(item, end=" ")
    print("]")

def swap(arr, num1, num2):
    temp = arr[num1]
    arr[num1] = arr[num2]
    arr[num2] = temp

def partition(arr, left, right):
    pivot = arr[right]
    leftPointer = left
    rightPointer = right - 1

    while True:
        while leftPointer <= right and arr[leftPointer] < pivot:
            leftPointer += 1

        while rightPointer >= left and arr[rightPointer] > pivot:
            rightPointer -= 1

        if leftPointer >= rightPointer:
            break
        else:
            print("Item swapped:", arr[leftPointer], ",", arr[rightPointer])
            swap(arr, leftPointer, rightPointer)

    print("Pivot swapped:", arr[leftPointer], ",", arr[right])
    swap(arr, leftPointer, right)

    return leftPointer

def quickSort(arr, left, right):
    if right <= left:
        return
    else:
        partitionPoint = partition(arr, left, right)
        quickSort(arr, left, partitionPoint - 1)
        quickSort(arr, partitionPoint + 1, right)

intArray = [4, 6, 3, 2, 1, 9, 7]
print("Input Array: ", end="")
display(intArray)
printline(50)
quickSort(intArray, 0, len(intArray) - 1)
print("Output Array: ", end="")
display(intArray)
printline(50)
      
                