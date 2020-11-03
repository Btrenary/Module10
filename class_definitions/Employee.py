"""
Author: Brady Trenary
Program: Employee.py


"""

from datetime import date


class Employee:
    """Employee class"""

    # Constructor
    def __init__(self, lname, fname, address, pnumber, salaried, sdate, salary):
        self.last_name = lname
        self.first_name = fname
        self.address = address
        self.phone_number = pnumber
        self.salaried = salaried
        self.start_date = sdate
        self.salary = salary

    def display(self):
        if self.salaried:
            return self.first_name + " " + self.last_name + "\n" \
                   + self.address + "\n" + self.phone_number + "\n" \
                   + "Salaried employee: $" + str(self.salary) + "/year" + "\n" + str(self.start_date)
        else:
            return self.first_name + " " + self.last_name + "\n" \
                   + self.address + "\n" + self.phone_number + "\n" \
                   + "hourly employee: $" + str(self.salary) + "/hour" + "\n" + str(self.start_date)

    def __str__(self):
        return "Employee: first name =" + str(self.first_name) + ', last name =' + str(self.last_name) + ', address =' \
               + str(self.address) + ', phone =' + str(self.phone_number) + ', salary =' + str(self.salary) \
               + ', start date =' + str(self.start_date) + ', salaried =' + str(self.salaried)

    def __repr__(self):
        return "Employee: first name =" + repr(self.first_name) + ', last name =' + repr(self.last_name) + ', address =' \
               + repr(self.address) + ', phone =' + repr(self.phone_number) + ', salary =' + repr(self.salary) \
               + ', start date =' + repr(self.start_date) + ', salaried =' + repr(self.salaried)


# drive
tdate = date.today()
empl = Employee('Trenary', 'Brady', '900 nowhere ave, Chariton IA 22233', '555-155-4888', True, tdate, 35000)
print(empl.display())
print(empl)

empl2 = Employee('Trenary', 'Brady', '900 nowhere ave, Chariton IA 22233', '555-155-4888', False, tdate, 10.50)
print(empl2.display())
print(repr(empl2))
