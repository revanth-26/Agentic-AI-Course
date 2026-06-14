"""
# Creating a function for an employee, BUT WE DO NOT USE FUNCTIONS IN PRODUCTION(COMPANY/ORGANIZATION) LEVEL.
def create_employee(first, last, pay):
    email=f"{first.lower()}.{last.lower()}@infosys.com"
    return {"first":first, "last":last, "email":email, "pay":pay}
emp1=create_employee("Rahul","deva",54000)
# If i want to increase the employee pay(salary) to some percentage value, then i have to create another function
def emp_pay_raise(employee,percentage):
    employee['pay']=int(employee['pay']*(1+percentage/100))
print(emp1) #o/p: {'first': 'Rahul', 'last': 'deva', 'email': 'rahul.deva@infosys.com', 'pay': 54000}
emp_pay_raise(emp1,5) 
print(emp1) #o/p: {'first': 'Rahul', 'last': 'deva', 'email': 'rahul.deva@infosys.com', 'pay': 56700}

emp1_first="Rahul"
emp1_last="deva"
emp1_email="rahul.deva@infosys.com"
emp1_pay=54000

emp2_first="John"
emp2_last="Doe"
emp2_email="john.doe@infosys.com"
emp2_pay=64000

#we can conclude that by using "Functions" concept, we should create mulitple functions for each operation, it took more space and code looks bad. so to overcome this problem we should use "class" and other oops concepts to store more amount of info.
"""
#CLASS
class Employee: #Inside the class, "methods" will be there 
    def __init__(self, first,last,pay): #To define the parameters inside the method, "self" is used. "__init__()" method will be executed automatically. "__init__" method is ran only once when an object is instantiated (created). 
        self.first=first    #on the left part of equals to after "self." we can give any name, but according to the industry standards we should give the name what we have given on the right side after equals to, so that it is very easy understand.
        self.last=last
        self.pay=pay
        self.email=f"{first.lower()}.{last.lower()}@gmail.com"
    #We can Add "custom Methods" inside a class
    def full_name(self):
        return f"{self.first} {self.last}" #we cannot directly access the parameters which are inside the "init" method from outside "init" method, so to access them we should write "self." before those parameters to access them.and
    #We can also increase the salary of a particular employee by creating custom methods
    def increase_pay(self, percentage):
        self.pay=int(self.pay*(1+percentage/100))
#OBJECT FOR THIS CLASS
emp1=Employee("Rahul", "Deva", 60000)
print(emp1.last) #then, "self" will be replaced with "emp1" i.e., object / instance name
print(emp1.pay)
emp1.increase_pay(5)
print(emp1.pay)
emp2=Employee("Satya", "Dev", 78333)
print(emp2.first)
print(emp2.email)
print(emp1.full_name())
print(emp2.pay)
emp2.increase_pay(10)
print(emp2.pay)
#so by this we can conclude that we can reuse the class code number of times by using objects
 
#INSTANCE VARIABLES-each instance has it's own data
print(emp1.first)  #Rahul
print(emp2.first)  #Satya
#changing one variable's value does not affect the other variables
emp1.pay=40000
print(emp1.pay)   #40000 (changed)
print(emp2.pay)   #78333 (unchanged)

#Printing the employee details in dictionary format
print(emp1.__dict__)  #{'first': 'Rahul', 'last': 'Deva', 'pay': 40000, 'email': 'rahul.deva@gmail.com'}

"""
#WE CAN CALL A METHOD IN 2 WAYS
1. emp1.increase_pay(5)
2. Employee.increase_pay(emp2,5)
"""