# Python Program - Name Validation.

def name_Validation(name):
    for char in name:
       if not(char.isalpha() or char == ' '):
           return False
    else:
        return True
name = input('Enter Any Name : ')
if name_Validation(name):
    print(name, 'is a Valid Name')
else:
    print(name, 'is not a Valid Name')