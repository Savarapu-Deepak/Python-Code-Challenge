# Python Program to create Dictionary of Employees.

def Employee(emp, n):
    for i in range(n):
        Name = input('Enter Employee Name : ')
        salary = int(input('Enter Employee Salary : '))
        print('-' * 25)
        emp[Name] = salary
emp = {}
n = int(input('No.of.Employees : '))
Employee(emp, n)
print(emp)