"""
CLASS METHOD:
->It is a method whose first parameter is "cls". (we don't need any "self" parameter)
--> where, 'cls' means 'class'. Imagine we are not providing the instance(i.e., self) of a class as the parameter, instead we are providing a "complete class" itself. 
If i want to make a method as 'class method', then i want a "Decorator" i.e., "@classmethod", By using this decorator we are saying to python to make the method as classmethod.

Q) When it is used?
ans:    1. When we want to modify(at once) a variable that every single instance shares.
        2. When we are working with "class variables"
"""


class Employee:
    raise_percentage = 1.04 #class/global variable
    num_of_employees = 0
    company = "Infosys"

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@{Employee.company.lower()}.com"
        Employee.num_of_employees += 1

    def full_name(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):      #method to increase the salary of an emp
        self.pay = int(self.pay * self.raise_percentage)
    
    @classmethod
    def get_count(cls):        #method to count the number of employees
        return cls.num_of_employees  # we made it as a class method because, we cannot write as "emp1.num_of_employees", so we did not reuire "self" here, so we should make it as a "class method".
    
    @staticmethod
    def is_workday(day):  #method to find whether the particular day is working day or not 
        return day.weekday() < 5       # 0 is Monday and 6 is Sunday

    @classmethod
    def set_raise_percentage(cls, amount):  #Here, we are passing the entire class
        cls.raise_percentage = amount
print(Employee.raise_percentage)    #1.04

#set the raise_percentage to 1.07 for all the employees
Employee.set_raise_percentage(1.07) # No instance needed
print(Employee.raise_percentage)    #1.07

#set the raise_percentage to 1.10 for specific employees
emp1=Employee("Revanth", "Reddy", 100000)
emp2=Employee("Zombie", "Reddy", 400000)

Employee.set_raise_percentage(1.10)

print(emp1.raise_percentage)
print(emp2.raise_percentage)

#To count number of employees
#Before
print(Employee.get_count()) # 2  - no instance needed

Employee("A", "jfdf", 235564)
Employee("B", "jakka", 235564)
Employee("C", "tempa", 235564)

#After
print(Employee.get_count())  # 5

#i.e, we can set the values at class variable level

#checking the particular day is 'workday' or not 
import datetime

work_date = datetime.date(2026, 5, 22)
week_end = datetime.date(2026, 5, 24)

print(Employee.is_workday(work_date))   # True
print(Employee.is_workday(week_end))    # False

"""
STATIC METHOD:
-> It is a method which does not contains any 'first parameters'.
-> If i want to make a method as 'static method', then i want a "Decorator" i.e., "@staticmethod", By using this decorator we are saying to python to make the method as classmethod.

Q) When to use it?
ans: If there is no use of 'class' or 'instance' while we performing operations in a method then in that case we should create this method, i.e., if the method is not depends on the object's or class's data.
        1. Use it when the function does not require self (instance data) or cls (class data).
        2. Use it to check if data formats are true or false before processing them further.
        3. Use it to convert data types, formats, or units.
        4. Use it when the output depends entirely and solely on the inputs passed into it.

ex 1: in the above code "work day" static method.
ex 2:
class StringHelper:
    @staticmethod
    def to_snake_case(text):
        return text.lower().replace(" ", "_")
    @staticmethod
    def is_valid_email(text):
        return "@" in text and "." in text
        
print(StringHelper.to_snake_case("Hello world"))    # hello_world
print(StringHelper.is_valid_email("a@b.com"))       # True

we can also write the these type of methods (without defining the methods as "@staticmethod") outside the class, it will run successfully, but we should not write like this because when someone want to see that method they can also see by using "classname"  i.e., Employee.is_workday
"""
