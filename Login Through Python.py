# Python Program to Login Using Python.

for chance in range(3):
    user_Name = input('Enter User Name : ')
    password = input('Enter User Password : ')
    if user_Name == 'deepak' and password == 'python':
        print('Access Granted')
        break
    else:
        print('In-Correct User Details.')
else:
    print('Access Denied')