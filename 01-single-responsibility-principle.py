"""
a class should have single responsibility i.e. it should only change for one reason to change

"""

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def calculate_salary(self):
        # Salary calculation logic (based on position, hours worked, etc.)
        if self.position == "Developer":
            return 80000
        elif self.position == "Manager":
            return 95000
        else:
            return 50000

    def generate_report(self):
        # Generating employee report
        return f"Employee Report: {self.name}, Position: {self.position}, Salary: {self.calculate_salary()}"

    def save_to_database(self):
        # Saving employee details to a database
        print(f"Saving {self.name} to database...")


"""
In this example, the Employee class has multiple responsibilities:

1. Calculating salary.
2. Generating reports.
3. Saving employee details to a database.

"""


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class SalaryCalculator:
    @staticmethod
    def calculate(employee: Employee):
        if employee.position == "Developer":
            return 80000
        elif employee.position == "Manager":
            return 95000
        else:
            return 50000

class EmployeeReport:
    @staticmethod
    def generate(employee: Employee, salary: float):
        return f"Employee Report: {employee.name}, Position: {employee.position}, Salary: {salary}"

class EmployeeDatabase:
    @staticmethod
    def save(employee: Employee):
        print(f"Saving {employee.name} to database...")

# Usage
employee = Employee("Alice", "Developer")
salary = SalaryCalculator.calculate(employee)
report = EmployeeReport.generate(employee, salary)
EmployeeDatabase.save(employee)

print(report)





