class Employee:
    company_name = "CarMax"
    hike = 0.07
    total_Employee = []

    def __init__(self):
        self.firstname = input("Enter the employee First name: ")
        self.lastname = input("Enter the employee Last name: ")
        self.salary = float(input("How much you like to pay the employee: "))
        self.employee_details = {}
        Employee.total_Employee.append(self)

    def display_employee_details(self):
        self.employee_details["Full name"] = self.firstname + " " + self.lastname
        self.employee_details["Pay"] = self.salary
        self.employee_details[
            "E-mail"] = self.firstname.lower() + "." + self.lastname.lower() + "@" + Employee.company_name + "." + "com"
        self.employee_details["Net pay"] = self.salary + (self.salary * Employee.hike)
        return self.employee_details

    def display_employee_details1(self):
        print("Fullname:", self.firstname + self.lastname, "\n" "Pay:", self.salary, "\n" "Email: ",
              self.firstname.lower() + "." + self.lastname.lower() + "@" + Employee.company_name + "." + "com",
              "\n""Net Salary: ", self.salary + (self.salary * Employee.hike))

    def __repr__(self):
        return f"{self.employee_details}"


employee1 = Employee()
employee2 = Employee()
employee3 = Employee()
print(f"Employee_Details = {employee1.display_employee_details()}")
employee1.display_employee_details()
employee2.display_employee_details()
employee3.display_employee_details()
print(Employee.total_Employee)
