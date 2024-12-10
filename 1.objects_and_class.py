class Employee:
    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 6
    noOfWorkingHours = 40

    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Target has been achieved")
        else:
            print("Target has not been achieved")


employeeOne = Employee()
print(employeeOne.salesMadeThisWeek) # class attributes
print(employeeOne.hasAchievedTarget())
print(employeeOne.noOfWorkingHours)
employeeTwo = Employee()
print(employeeTwo.noOfWorkingHours) # class attributes

print("Changed class attribute hours to 60")
Employee.noOfWorkingHours = 60 # class attributes
print(employeeOne.noOfWorkingHours)
print(employeeTwo.noOfWorkingHours)

print("Changed class attribute hours to 60")
employeeOne.noOfWorkingHours = 80 # instance attributes
print(employeeOne.noOfWorkingHours)
print(employeeTwo.noOfWorkingHours)
