# Object Oriented Programming
To represent data and method 
## Class 
Blueprint for declaring and creationg objects
`class name`
## Object 
Instance of the class
```
Example
imagine class as mid term
data members and funtions as date time, slot of the exam etc
```
## Constructor and Destructor
**Constructor** : it will help you in initiasisation of the obj of the class
**Destructor** : 

## Syntax
```
class cname:
       def __init__(self,value):
           delf.value =value
           

```
going for outing how to use class and object


## Inheritance
It allows classes to inherit common properties for parent class
```
class Parent:
    def __init__(self, name):
        self.name = name
    
    def display_name(self):
        print(f"Parent name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the constructor of the parent class
        self.age = age
    
    def display_age(self):
        print(f"Child age: {self.age}")

# Create an instance of Child
child = Child("Alice", 10)
child.display_name()  # Inherited method from Parent class
child.display_age()   # Method from Child class

```
