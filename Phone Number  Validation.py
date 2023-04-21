# Phone Number Validation.

def phone_Validation(number):
    if len(number) != 10:
        return False
    elif not number.isdigit():
        return False
    elif number[0] not in '789':
        return False
    else:
        return True
number = input('Enter Mobile Number : ')
if phone_Validation(number):
    print(number, 'is a Valid Phone NUmber')
else:
    print(number, 'is not a Valid Phone Number')
