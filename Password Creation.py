# Python Prgoram to Generate a Strong Password.

password = input('Enter Your Password : ')
if len(password) >= 8 and len(password) <= 16:
    c, s, d, sp, n = 0, 0, 0, 0, 0
    for char in password:
        if char.isupper():
            c += 1
        elif char.islower():
            s += 1
        elif char.isdigit():
            d += 1
        elif char in '!@#$%^&*()_+_=/<>/?.,':
            sp += 1
        else:
            n += 1
            break
    else:
        if c > 0 and s > 0 and d > 0 and sp > 0:
            print(password, 'is a Strong Password')
        else:
            print(password, 'is a Weak Password')
else:
    print('Password must greater than 8 and less than 16 Characters.')
