#  Debugging,Error and Exception Handling

# Write a Python program that takes two numbers as input from the user.
try:
    num1  = int(input("Enter number1"))
    num2  = int(input("Enter number2"))
    
    
    result  = num1  / num2
    print(result)
except ZeroDivisionError:
    print("Error division by zero is not allowed")
    print("enter a number that is none zero")
    
    
"""
Exercise 2: Handling a FileNotFoundError
Write a Python program that asks the user to enter a file name.
Implement exception handling to handle the scenario where the specified file does not exist (FileNotFoundError).
Display an appropriate error message if the file is not found and ask the user to enter a valid file name.




"""

      
    