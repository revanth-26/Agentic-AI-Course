# INHERITANCE
class Employee: #parent class
    raise_percentage = 1.04 # Class variable or Global variable
    num_of_employees = 0    #to count the number of employees
   
    def __init__(self, first, last, pay):
        self.first = first  # instance(local) variable
        self.last = last    # instance(local) variable
        self.pay   = pay    # instance(local) variable
        self.email = f"{first.lower()}.{last.lower()}@infossy.com"
        Employee.num_of_employees += 1   # since "count" is a "Global" variable, we can directly access it using the classname.

    def full_name(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay= int(self.pay*self.raise_percentage)

#child class
class Developer(Employee):  #syntax of Inheritance: class child_classname(parent_classname):    ->  Now every developer is an employee
    pass
# why we do not write "__init__" method because, since, child class is inherited from the parent class, all the methods (characters) which are inside the parent class will shared to the child class.

"""
How inheritance will work?
ans: when we call any function / method (which is inside a parent class) from the child class, then 'python' searches in a specific order known as "Method Resolution Order (MRO).
    for example,
                dev1.full_name():
                step 1- Does the instance dev1 have it? # NO
                step 2- Does the class Developer (child class) have it? # NO
                step 3- Does the class Employee (parent class) have it? # YES - call it

""" 
dev1 = Developer("Rahul", "yadav", 400000)
    
print(dev1.full_name)
print(dev1.email)
print(dev1.pay)

dev1.apply_raise()
print(dev1.pay)


# we can also inherit the 'class variables' also.
class Developer2(Employee):
    raise_percentage = 1.10  # inherited and overrided class variable

dev2=Developer2("Racha", "ram", 493894)
emp1=Employee("janakiram", "pataas", 954554)

dev2.apply_raise()
emp1.apply_raise()

print(dev2.pay)
print(emp1.pay)


# super: if we want to add another parameter in the child class but not in the parent class then, "super" keyword comes into picture.
class Developer3(Employee):
    raise_percentage = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev3=Developer3("Rama", "raka", 493894, "python")

print(dev3.full_name)       # Rama raka
print(dev3.email)           # rama.raka@infossy.com
print(dev3.prog_lang)       # python


# Manager's class - there are number of employees works under the manager.
class Manager(Employee):
    raise_percentage = 1.05
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
   
    def add_employee(self, emp):
        if emp not in self.employees: 
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees: 
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print(f" --> {emp.full_name()}")

    #Encapsulation- when we want to make some changes with extra information in child class which are already present in the parent class then it is called as encapsultion.   
    def apply_raise(self):
        super().apply_raise()       # do what Employee normally does
        for emp in self.employees:  # then, adds manager-specific behaviour i.e., every "employee" who is working under the manager will get a bonus 1%.
            emp.pay = int(emp.pay * 1.01)   # 1% bonus to each report.
        
dev4 = Developer3("Rahul", "Sharma", 800000, "Python")
dev5 = Developer3("Priya", "Patel", 900000, "Java")

mngr1 = Manager("Amit", "Kumar", 1500000, [dev4])

mngr1.print_employees()
# -- > Rahul Sharma

mngr1.add_employee(dev5)
mngr1.print_employees()
# -- > Rahul Sharma
# -- > Priya Patel

mngr1.remove_employee(dev4)
mngr1.print_employees()
# -> Priya Patel

#suppose infosys decided:
#when a Manager gets a raise, evey developer reporting to them gets a small bonus too.
# The plain 'apply_raise' from 'Employee' class does not know anything about 'reports' - it just bumps(updates/increases) "self.pay"
# We need "Manager.apply_raise" to do something extra, so we override it:  -  "apply_raise" method of 'manager is in the "Manager" class.

dev6 = Developer3("Rahul", "Sharma", 800000, "Python")
dev7 = Developer3("Priya", "Patel", 900000, "Java")

mgr1 = Manager("Amit", "Kumar", 1500000, [dev1, dev2])

print("Before:")
print(f" Manager: Rs.{mgr1.pay:,}")
print(f" {dev6.first}: Rs.{dev6.pay:,}")
print(f" {dev7.first}: Rs.{dev7.pay:,}")

mgr1.apply_raise()

print("\n After manager's raise:")
print(f" Manager: Rs.{mgr1.pay:,}")
print(f" {dev6.first}: Rs.{dev6.pay:,}")
print(f" {dev7.first}: Rs.{dev7.pay:,}")

# Polymorphism - If we want to write the method name in the child class which is already present in the parent class, but we need to change complete functionality inside that method/function , then it is called as "polymorphism". 