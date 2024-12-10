class Employee():
    def __init__(self, name):
        self.name = name
    def employee_details(self):
        print(self.name)

    def print_employee_details(self):
        print(self.name)


emp_one = Employee('Siva')
print(emp_one.employee_details())
# print(Employee.employee_details().name) # error as name variable is not accessible

print(emp_one.print_employee_details())