# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=1
# Python Object Oriented Programming

# import datetime

class Employee:

    num_of_emps = 0
    raise_amount = 1.04                                 # class variable

    def __init__(self, first, last, pay):               # constructor, self = instance by convention
        self.first = first                              # attributes of our class
        self.last = last                                # instance variables
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    @property
    def fullname(self):                                 # method
        return '{} {}'.format(self.first, self.last)
    
    @fullname.getter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):                  # cls = class variable
        cls.raise_amount = amount

    # alternate constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod                                       # if we don't need instance of the class within the function
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    def __repr__(self) -> str:
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self) -> str:
        return '{}-{}'.format(self.fullname, self.email)

emp_1 = Employee('Corey', 'Schafer', 5000)      # instances, instance is passed automatically
emp_2 = Employee('Test', 'User', 6000)

print(emp_1)
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))
print(emp_1.fullname)

# new_emp = Employee.from_string('first-last-1000')
# print(emp_1.__dict__)                                   # namespace
# print(Employee.__dict__)                                # namespace

# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())
# print(Employee.fullname(emp_1))