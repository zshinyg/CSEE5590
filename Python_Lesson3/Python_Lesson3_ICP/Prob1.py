#1. Create a class Employee and then do the following
#       Create a data member to count the number of Employees
#       Create a constructor to initialize name, family, salary, department
#       Create a function to average salary
#       Create a Fulltime Employee class and it should inherit the properties of Employee class
#       Create the instances of Fulltime Employee class and Employee class and call their member functions.



class Employee:
    totalEmployees = 0
    totalSalary = 0

    def __init__(self,name,family,salary,department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.totalEmployees = Employee.totalEmployees + 1
        Employee.totalSalary = Employee.totalSalary + self.salary

    def averageSalary():
        return Employee.totalSalary/Employee.totalEmployees


class FullTimeEmployee(Employee):
    def __init__(self, name,family,salary,department):
        Employee.__init__(self,name,family,salary,department)




myEmployee1 = Employee("Coltyn", "Gatton", 100000, "Sales")
myEmployee2 = Employee("Lake", "Gatton", 120000, "Data Migration")
myEmployee3 = FullTimeEmployee("Jennifer", "Heronema", 80000, "Research")

print("\n\n")
print( "%s %s:\n" "     Salary: $%d\n     Department: %s" % (myEmployee1.name, myEmployee1.family, myEmployee1.salary, myEmployee1.department))
print( "%s %s:\n" "     Salary: $%d\n     Department: %s" % (myEmployee2.name, myEmployee2.family, myEmployee2.salary, myEmployee2.department))
print( "%s %s:\n" "     Salary: $%d\n     Department: %s" % (myEmployee3.name, myEmployee3.family, myEmployee3.salary, myEmployee3.department))

print("\nAverage Salary: $%d\n" % (myEmployee1.__class__.averageSalary()))


    