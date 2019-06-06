class Employee(object):
    raise_amt = 1.04

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    def pay(self):
        pass

    def email(self):
        pass

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)

emp_2 = Employee('Test', 'Employee', 60000)

import datetime
my_date = datetime.date(2016, 7, 11)
print(" IS MY "+my_date+"Working data?",Employee.is_workday(my_date))


#distructor
class Greeting:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print ("Destructor started")

    def SayHello(self):
        print ("Hello", self.name)



