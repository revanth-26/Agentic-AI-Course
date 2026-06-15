"""
"__slots__" function:
The __slots__ attribute should be a list or tuple containing the names of the attributes we want to store in slots.
ex:
class MyClass:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age
Here, "MyClass" instances will only have the "name" and "age" attributes, and if attempts to add other attributes will result in an error.
What happens if we do not use "slots"?
ANS: If we do not use"slots", then at some some point we may type wrong variable name, for example -> age to aeg, name to nmae,... In this case, python will not throw any any error and allocates memory to the new variable what we have typed wrongly. So, it is very useful to use "slots" in production level. 
"""
"""
#Implementation 
#Without using '__slots__'
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
emp1=MyClass("Rahul",26)
print(emp1.__dict__)   #{'name': 'Rahul', 'age': 26}
emp1.aeg=21
print(emp1.__dict__)   #{'name': 'Rahul', 'age': 26, 'aeg': 21}
"""
"""
#Using '__slots__'
class MyClass:
    __slots__ = ['name', 'age']
def __init__(self, name, age):
        self.name = name
        self.age = age
emp1=MyClass("Rahul",26)
print(emp1.__dict__)   
emp1.aeg=21
print(emp1.__dict__)  #o/p: emp1=MyClass("Rahul",26) -> TypeError: MyClass() takes no arguments
"""

#CLASS VARIABLES - class variables are variables that are shared(applicable) across all instances (objects) of a class. They are defined inside the class body but outside any instance methods or the __init__ constructor.
# if the particular variable is same for all instances then, define that variable as a "Global variable".abs
# if the particular variable is different for different instances then, they are "instance(local)" variables.
class Employee:
    raise_percentage = 1.04 # Class variable or Global variable
    count = 0    #to count the number of employees
    __slots__ = ["first", "last", "pay", "email"] # This is enforcing python.
    def __init__(self, first, last, pay):
        self.first = first  # instance(local) variable
        self.last = last    # instance(local) variable
        self.pay   = pay    # instance(local) variable
        self.email = f"{first.lower()}.{last.lower()}@infossy.com"
        Employee.count += 1   # since "count" is a "Global" variable, we can directly access it using the classname.
    def full_name(self):
        return f"{self.first} {self.last}"
    def increase_pay(self):
        self.pay= int(self.pay*self.raise_percentage) # 4%
emp1 = Employee("Rahul", "Sharma", 800000)
emp2 = Employee("Priya", "Patel", 900000)
# Access through the class
print(Employee.raise_percentage)   # 1.04
# Access through instances
print(emp1.raise_percentage)       # 1.04
print(emp2.raise_percentage)       # 1.04
emp1.increase_pay()
print(emp1.pay)
#How a class variable works?
# ans: First of all python will check the particular variable in particular instance dictionary(ex: emp1.__dict__), if it is not found then, it will checks inside the class. If Still it was not found then it will throw an "attribute error". 
print(Employee.count)    #To know the number of employees in a company
#changing raise percentage of all instances(employees) at a time
Employee.raise_percentage=1.07
print(Employee.raise_percentage)

#changing raise percentage of specific instance(employee) 
emp1.raise_percentage=1.15 #it will only change the salary of "emp1", but not for other employees.
print(emp1.raise_percentage)
