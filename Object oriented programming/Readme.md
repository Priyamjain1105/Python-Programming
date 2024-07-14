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

## Constructor (_ _ init _ _ Funtion)
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
<br>
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
Types:  
**1. Static Method:** Method in which neither self is used, nor any changesa are made  
**2. Class Method:** Method in which we want to make changes in class attributes  
**3. Instance Method:** Method with self attribute  

Creating instance method in class
```
class Student:
      def __init__(self,marks,name):
          self.marks = marks
          self.name - name

      def welcome(self):
          print(self.name)
          return self.marks
```
### Static Methods
The functions that are not using the object(self) values are static methods, these function dont have self parameter
```
class Student:
      @staticmethod   #decorater
      def college():
           print("ABC College")
```
**Decorater:** modifies the property of the function,(temporarily) 
it allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.


# FOUR PILLARS OF OOP'S [AEIP]
# Abstraction 
Hiding the implementation detail of a class and only showing the essential features to the user  
Example Stating Automated Car
```
class Car():
      def __init__(self):
          self.acc = False
          self.brake = False
          self.clutch = False

      def Start(self):
          self.acc = True
          self.acc = True
          print("Car Started...")
car1 = Car()
Car1.start()
```
output: `Car Started...`
### Private (like) Attributes and Methods (__pvt)
Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.   

1. Private attributes : using two underscores (_ _) before the var
   `__self.accpasswd = acc_pass`
2. Private method : using two underscores (_ _) before the function name
   ```
   def __transaction(ano,bal):
        print("Performs Transaction")
   ```
Note: In python we conceptually implement private, they are not reallhy private
       



# Encapsulation (Capsule)
Wrapping data and function into a single unit (object).

### Question
Create Account class with 2 attributes - balance and account no. Create Methods for debit, credit and printing the balance.
```
class Account():
      def __init__(self,ano,bal):
          self.ano = ano
          self.bal = bal

      def credit(self,ano,amt):
          self.bal = slef.bal+amt
          print("Money Credited Succesfully")
          self.get_balance()

      def  debit(self,ano,amt):
           self.bal = self.bal-amt
           print("Money Debited Succesfully")
           self.get_balance()
       
      def get_balance():
          print("A.no:",self.ano,"\nBalance:",self.bal")
     
a1 = Account(1,200)
a1.credit(1,900)
a1.debit(1,450)
          
```
# Inheritance
When one class derives the property of another class.
```
class Car:              # Parent Class
      @staticmethod
      def start():
          print("Car Started...")

      @staticmethod
      def stop():
           print("Car Stopped...")

class ToyotaCar(Car):     # Child Class
       def __intit__(self,name):
           self.name = name
car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

        
```
## Types of Inheritance
#### 1. Single Inheritance: `One base class -> one derive class`
#### 2. Multi-Level Inheritance: `parent_class -> child -> grand_child`
```
   class Fortuner(Toyota_Car):
         def __intit__(self,type):
            self.type = type
   
   car1 = Fortuner("disel")
   car1.start() 
```
#### 3. Multiple Inheritance: `class derived from multiple classes`
   ```
   class A:
        varA = "welcome to class A"

   class B:
         varB = "Welcome to class B"
   
   class C(A,B):
         varC = "welcome to class C"
   
   ```
### Super Method
   `Super()` method is used to access methods of the parent class.  
   Sometimes we have to change the values in parent class through child class,or access methods from child class, to do that we have Super Method

Example Calling the super constructor (parent class constructor)
```
class ToyotaCar(self,name,type):
      super().__init__(type)
      self.name = name
```
### Class Method
A class method is bound to the class & receives the class as an implict first argument
Ways of changing the values of class Attributes
1.Through class keyword
```
class Person:
      name = 'anonymous`

      def changeName(self. name):
          Person.name = name
```
2. Through class keyword
```
class Person:
      name = 'anonymous`

      def changeName(self. name):
          self.__class__.name = name
```
`p1 = Person`  
`p1.changeName("rahul kumar")`

3. Through class method
   ```
   @classmethod
   def changeName(cls,name):
       cls.name = name
   ```

# Polymorphism (Many-Forms/Anak-Ekum)
### Operator Overloading
When the same Operator is allowed to have different forms/meaning/usuage according to the context
```
print(1+2)                # 3         used for adding int (defined in class int)
print("Pri" + "yam")      # Priyam    used for adding string  (defined in class string)
print([1,2,3] + [3,4,5])  # merge     used for adding  list (defined in class list)
```


# Important Keywords
1. Delete attribute:  `del s1.name` | Delete object:  `del s1`

# Decorator
1. `@staticmethod`: makes a method static
2. `@classmethod`: makes the method class method
3. `@property`/attribute: when one attribute depends on another attributes, and (changing the value of one wont change the value of another)
so when we cannot give any fixed value to attribute then its value will depende on any method, to use the method as an attribute
```
class Student:
      def __init__(self,phy,chem,math):
          self.phy = phy
          self.chem = chem
          self.math = math

      # percentage function will act like attribute, but is function returning the value
      @property
      def percentage(self):
           self.percentage = str((self.phy  + self.chem + self.math))/3)+"%"

stu1 = Student(98,97,99)

stu1.phy = 86
print(stu.phy)
print(stu1.percentage)
```
4. `@getter`
5. `@setter`





