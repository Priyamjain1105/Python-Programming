# Why do we need Function 
Funtions were created for re-useablity of code and decresing reduntancy  
And similarly for increaseing the reduntancy of the code we have OOP's

# Class & Object in Python
Class is a blueprint for creating objects
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
