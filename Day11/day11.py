
""""


1. Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"
Use 'assign_department' method to change the department of an employee.
Use 'print_employee_details' method to print the details of an employee.
Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
overtime = hours_worked - 50
Overtime amount = (overtime * (salary

"""







class  Employee:
    
    def __init__(self,name,emp_id,salary,department):
        
        #initializing the instance of the class
        self.name = name
        self.id = emp_id
        self.salary = salary
        self.department = department
        
    # method to calculate salary
    
    
    def calculate_salary(self,salary,hours_worked):
        overtime  = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        self.salary = self.salary + (overtime * (self.salary/ 50))
        
        # using assign department to change  department of an employee
    def  assign_department(self,emp_department):
        self.department = emp_department    
            
          
# method to print employee details
    def print_employee_details(self):
        print("\nName:", self.name)
        print("ID:",self.id)
        print("salary:", self.salary)
        print("Department:",self.department)
        print("----------------")
        
        
    
    #creating instance of already defined class and assigning data to it
    
employee1  = Employee("ADAMS","E7877",50000,"ACCOUNTING")
employee2  = Employee("VINCENT","E7877",600000,"Webdeveloper")
employee3  = Employee("Daniel","Et667",70000,"Cloud-Computing")
employee4  = Employee("Donda","E788",80000,"Andrioddev")
employee5  = Employee("Magie","Et678",120000,'Designer')

#printing details being accessed in our classes
print('Original Employee  Details: ')
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()
employee5.print_employee_details()


#changing department of employee 1 and 5
employee1.assign_department("Journalist")
employee5.assign_department("programmer")

# printting updated employee

print("Updated Employee Details :")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()
employee5.print_employee_details()


"""
2. Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.

"""

class BankAccount:
    
    def  __init__(self,account_number,balance,date_of_opening,customer_name):
        
        
     #creating instance of already defined class and assigning data to it
     self.account_number  = account_number
     self.balance  = balance
     self.date_of_opening = date_of_opening
     self.customer_name  = customer_name
     
     
    #  method to deposit in bank account
    
    def deposit(self,amount):
        self.balance += amount
        print(f"$amount  has been deposited in your account.")
      
      
    def widthdraw(self,amount):
        if amount > self.balance:
             print("insufficient balance.")
        else:
            self.balance  -= amount
            print(f"${amount} has been withdrawn from your account.")
            
       # method to check balance 
    def check_balance(self):
        print(f"current balance is ${self.balance}.")
    
    #method that prints customer details
    def print_customer_details(self):
        print("Name:",self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of opening:", self.date_of_opening)
        print(f"Balance: ${self.balance}\n")
        
        
        



#input customer details  through instance of a class
account1 = BankAccount(2245,50000, "01-01-2022","Vincenttommi")
account2  = BankAccount(590089,60000,"03-04-2021","Daniel Karanja")
account3  = BankAccount(6345,70000,"06-05-2022","calvin Arieri")
account4  = BankAccount(7241,80000,"07-08-2018","Diana Nyagano")
account5  = BankAccount(4567,50000,"05-08-2016","maxwell rono")
account6 = BankAccount (6789,434000,"03-9-2014","Simon mwangi")

                
                   
                
 #printing details of the customer
 
account1.print_customer_details()
account2.print_customer_details()
account3.print_customer_details()
account4.print_customer_details()
account5.print_customer_details()
account6.print_customer_details()
    
    
print("===================")
account6.print_customer_details()


#invoking arguments money via our methods
account4.deposit(2000)
account4.check_balance()

account4.widthdraw(50000)
account4.check_balance()    
        
    
account4.widthdraw(40000)
account4.check_balance()

# Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. Print all the attributes of the student1, student2 instances with their values in the given format


        
class Student:
    def __init__(self, name):
        self.name = name

    def print_student_details(self):
        print("Student:", self.name)

# Creating instances of the Student class
s1 = Student('vincenttommi')
s2 = Student('Daniel Karanja')

# Printing out the details of the students
s1.print_student_details()
s2.print_student_details()
 

    
     
        
            