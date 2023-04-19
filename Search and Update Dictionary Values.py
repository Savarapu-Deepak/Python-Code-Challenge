# Search and Update Dictionary Value.

def create_Employee(emp, n):
    for i in range(n):
        Name = input('Enter Employee Name : ')
        salary = int(input('Enter Employee Salary : '))
        emp[Name] = salary
def search_Employee(emp, name, percenatge):
    if name in emp:
        emp[name] = emp[name] + emp[name] * (percentage / 100)
        print(emp)
    else:
        print('No Such Directory with name {}'.format(name))
emp = {}
n = int(input('Enter No.of.Employees : '))
create_Employee(emp, n)
print(emp)
name = input('Enter Employee Name : ')
percentage = int(input('Enter Increse Amount in Percentage : '))
search_Employee(emp, name, percentage)