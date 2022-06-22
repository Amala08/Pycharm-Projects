class Employee:

    def __init__(self,firstname,lastname,salary,dob):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.dob = dob


    def display_employee_details(self):
        pass

    def no_of_args(*args):
        return(len(args))

emp1 = Employee("Amala","hari","1000", "08")
print(emp1.no_of_args("Amala","hari","1000","08"))
