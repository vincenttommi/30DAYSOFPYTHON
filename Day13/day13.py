#open the file in write mode

with open("output.txt","w") as file:
    
    #writing sentence to the file
    file.write("Hello,World")
    
    
    
    
    
    # Given a file named "numbers.txt" containing a list of integers separated by spaces, write a Python function to read the file and return the sum of all the numbers.
    
    
    
def calculate_sum(filename):
    total_sum = 0
    
    
    #open the file in read mode
    with open(filename,"r") as file:
        
        #reading the contents  of the file
        contents  =  file.read()
        
        
    #splitting the contents into a list of numbers 
     
    numbers  = contents.split()
    
    
    #convert the numbers from strings to integers and calculate  the sum
    
    total_sum =  sum(int(num) for num in  numbers)

    
    return total_sum

filename  = "numbers.txt"
result  = calculate_sum(filename)


        
    
    
           
