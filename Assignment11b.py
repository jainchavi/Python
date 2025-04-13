#Chavi Jain
#Batch 3
# Jecrc University


'''
A company has a database of employees, and the HR department needs a system to query employee details efficiently. Each employee has the following attributes: , , , , and . The system should handle two types of queries:: Given an employee ID, retrieve and display all details of the employee.: Given a department name, retrieve and display the names and salaries of all employees in that department, sorted by salary in descending order.
The first line contains T (1≤T≤10), the number of test cases.
The first line of each test case contains N (1≤N≤1000) and Q (1≤Q≤100), space-separated, denoting the number of employees and the number of queries.
The next N lines contain a tuple of 5 fields: , , , , and  (It's guaranteed that no two employees have the same Employee ID).
The next Q lines contain a query:
If the query starts with id:, it is an . The rest of the line contains the Employee ID.
If the query starts with dept:, it is a . The rest of the line contains the department name.
For each , print the details of the employee in the following format:CopyEmployee ID: <id>
Name: <name>
Department: <department>
Salary: <salary>
Joining Date: <joining date>
For each , print the names and salaries of all employees in the department, sorted by salary in descending order:CopyEmployees in <department>:
<name1>: <salary1>
<name2>: <salary2>
...
If no employee is found for a query, print No details found.
1≤T≤10
1≤N≤1000
1≤Q≤100
Employee IDs are unique.
Department names may contain spaces.
Salaries are positive integers.
Joining dates are in the format YYYY-MM-DD.
'''


class Employee:
    def __init__(self, emp_id, name, department, salary, joining_date):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = int(salary)
        self.joining_date = joining_date

class EmployeeDatabase:
    def __init__(self):
        self.employees = {}
        self.departments = {}

    def add_employee(self, emp_id, name, department, salary, joining_date):
        emp = Employee(emp_id, name, department, salary, joining_date)
        self.employees[emp_id] = emp
        if department not in self.departments:
            self.departments[department] = []
        self.departments[department].append(emp)

    def query_by_id(self, emp_id):
        if emp_id in self.employees:
            emp = self.employees[emp_id]
            print(f"Employee ID: {emp.emp_id}\nName: {emp.name}\nDepartment: {emp.department}\nSalary: {emp.salary}\nJoining Date: {emp.joining_date}")
        else:
            print("No details found.")

    def query_by_department(self, department):
        if department in self.departments:
            employees = sorted(self.departments[department], key=lambda x: -x.salary)
            print(f"Employees in {department}:")
            for emp in employees:
                print(f"{emp.name}: {emp.salary}")
        else:
            print("No details found.")

# Input data
t = 1  

# Test case 1
db = EmployeeDatabase()

employees = [
    ("101", "Alice", "HR", "50000", "2020-05-10"),
    ("102", "Bob", "IT", "60000", "2019-08-21"),
    ("103", "Charlie", "IT", "55000", "2021-03-15")
]

queries = [
    "id: 102",
    "dept: IT",
    "id: 105"
]

for emp in employees:
    db.add_employee(*emp)

for query in queries:
    if query.startswith("id:"):
        db.query_by_id(query.split("id: ")[1])
    elif query.startswith("dept:"):
        db.query_by_department(query.split("dept: ")[1])

