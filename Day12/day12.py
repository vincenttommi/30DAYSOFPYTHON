"""

.Inheritance: Create a class called Animal with a method speak() that prints "The animal makes a sound." Create two subclasses, Dog and Cat, which inherit from the Animal class. Override the speak() method in each subclass to print "The dog barks" and "The cat meows" respectively. Create instances of both subclasses and call their speak() methods

"""

# python inheritance syntax

#defining a  superclass

# example of python iheritance

class Animal:
    #attribute and  method of the parent class
    
    def eat(self):
     print("I can eat")
     

    #inheriting fron Animal
    
class Dog(Animal):
    # new method in subclass
    
    def display(self):
        # accessing name attribute of superclass using  self
        print("My name is ",self.name)
        
        
        
        
        
        
 #creating an object of  the subclass
labrador = Dog()


#acessing  superclass attribute  and method
labrador.name = "Vincent"
labrador.eat()


#calling a subclass method
labrador.display()
 
         
        
        
        