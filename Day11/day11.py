
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


    