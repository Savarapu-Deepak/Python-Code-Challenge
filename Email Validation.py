# Python Program to Print a Email Validation Program.

email = input('Enter Email ID : ')
if email.endswith('.com'):
    if email[0] != '@' and email.count('@') == 1:
        for ch in email:
            if ch.isalpha() or ch.isdigit() or ch == '%' or ch == '.' or ch == '@' or ch == '_':
                continue
            else:
                print('Not a Valid Email')
                break
        else:
            print('Valid Email')
    else:
        print('Not a Valid Email')
else:
    print('Not a Valid Email')