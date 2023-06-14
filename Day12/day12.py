"""

.Inheritance: Create a class called Animal with a method speak() that prints "The animal makes a sound." Create two subclasses, Dog and Cat, which inherit from the Animal class. Override the speak() method in each subclass to print "The dog barks" and "The cat meows" respectively. Create instances of both subclasses and call their speak() methods

"""

# python inheritance syntax

#defining a  superclass

# example of python iheritance

# class Animal:
#     #attribute and  method of the parent class
    
#     def eat(self):
#      print("I can eat")
     

#     #inheriting fron Animal
    
# class Dog(Animal):
#     # new method in subclass
    
#     def display(self):
#         # accessing name attribute of superclass using  self
#         print("My name is ",self.name)
        
        
        
        
        
        
#  #creating an object of  the subclass
# labrador = Dog()


# #acessing  superclass attribute  and method
# labrador.name = "Vincent"
# labrador.eat()


# #calling a subclass method
# labrador.display()
 
         
        
        
class Animal:
    
    def speak(self):
        print("The animal makes a sound.")
        
        
    # creating a subclass that inherits from Animal class
class Dog(Animal):
    def speak(self):
        print("The Dog Barks")
    
 #overridding speak method in each class
 
class Cat(Animal):
    def speak(self):
       print("The cat meows")
        
  
#creating instances of the classes and assigning it to the methods
dog = Dog()
cat = Cat()

  
#calling the methods assigned to the classes

cat.speak()
dog.speak()  
    
        



"""


 #Polymorphism : Create a class called Shape with an abstract method area(). Implement two subclasses, Circle and Rectangle, which inherit from the Shape class. Override the area() method in each subclass to calculate and return the area of a circle and rectangle respectively. Create instances of both subclasses and call their area() methods
Polymorphism is a very important concept in programming. It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.


"""

import math


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Creating instances of the subclasses
c1 = Circle(50)
rect = Rectangle(50, 40)

# Calling the area() methods
circle_area = c1.area()
rectangle_area = rect.area()

# Printing the results
print("Area of the circle:", circle_area)
print("Area of the rectangle:", rectangle_area)

    
 
      
            
        
        
        
    
    
    