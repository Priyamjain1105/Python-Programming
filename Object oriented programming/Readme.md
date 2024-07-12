# Why do we need Function 
Funtions were created for re-useablity of code and decresing reduntancy  
And similarly for increaseing the reduntancy of the code we have OOP's

# Class & Object in Python
Class is a blueprint for creating objects, collection of attributes and methods.
Creating Class  
```
class Student:
       name = "Priyam jain"
```
Creating Objects  
```
s1 = Student()
print(s1)
```
Notes  
1. Class name should be capital

## Constructor _ _ init _ _ Funtion
A class have a __init__ function, which is always executed when the object is being intiated.  
Default Constructor
```
class Student:
      def __init__():
          pass
```
Parametrized Constructor
```
def __init__(Self,name,marks)
    self.name = name
    self.marks = marks
```
Constructor always takes an argument, which is called as **self** parameter
**self**: Self parameter is the reference to current instance of the class, and is used to aCcess variables that belongs to the class
Notes:
1. constructer always has self argument
2. if dont create constructor, python it self creates constructors for us
3. self is always the first paramenter in the constructor
3. self is used to access the variables of the class
4.  a class can have more than one constructor

## Class & Instances Attributes
1. **Class Attribute:** the values which we do not want to change for many objects
2. **Object Attribute:** the values which we want unique for every object
They both are similar to global variable, major differnece is class attribute is same for all objects and object attricbute is unique to every object
```
class Student:
      college = "VIT Bhopal"            # Class Attribute
      def __init__ (self, name, marks) 
                   self.name = name     # Object Attribute
                   self.marks = marks
           
      s1 = Student("Priyam",17)
      s2 = Student("Sanket",20)
     
```
Note:
1. When there is same name class and object attribute then precedence of object attribute is more than class attribute
Modifying Class Attribute and Object attribute
```
class Example:
    class_attribute = "I am a class attribute"

    def __init__(self, value):
        self.instance_attribute = value  # Instance attribute

# Creating instances
example1 = Example(10)
example2 = Example(20)

# Accessing class attribute (Directly)
print(Example.class_attribute)  # Outputs: I am a class attribute
# Modifying class attribute using class name
Example.class_attribute = "Modified class attribute"

# Modifying class attribute using instance (creates an instance attribute with the same name)(Through Instance)
example1.class_attribute = "Instance specific attribute"

# Accessing instance attributes
print(example1.instance_attribute)  # Outputs: 10
print(example2.instance_attribute)  # Outputs: 20

```



## Methods
Functions when used in class is called methods  
Creating method in class
```
class Student:
      def __init__(self,marks,name):
          self.marks = marks
          self.name - name

      def welcome(self):
          return marks
```

