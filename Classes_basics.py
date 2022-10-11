class Employee:
    
    increment = 1.5 #class variable....
    no_of_employees = 0
    
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees += 1  #uses the class Variables
     
    def increase(self):
        self.salary = self.salary * Employee.increment
    
    @classmethod   #clas decorator
    def change_increment(cls, amount):
        cls.increment = amount
    
    @staticmethod  #class decorator to creat normal functions
    def isopen(day):
        if day == 'sunday':
            return False
        else:
            return True
        
#inheritance

class Programmer(Employee):
    
    def __init(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary) # calls the init function of the parent class
        self.proglang = proglang
        self.exp = exp
    
print(Employee.no_of_employees) #initially the no of employees is zero
harry = Employee('Harry', 'Jackson', 44000)
print(Employee.no_of_employees)  #now 1 new Employee gets added
rohan = Employee('Rohan', 'Das', 44000)
print(Employee.no_of_employees)  #now total 2 employees are there

print(harry.salary)
Employee.change_increment(2)  #changes the increment value to 2
harry.increase()
print(harry.salary)

print(Employee.isopen('sunday'))

