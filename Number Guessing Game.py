# Number Guessing Game Using Python.

import random

num = random.randint(1, 100)

chances = int(input('Enter No.of.Chances You Want : '))

for chance in range(1, chances + 1):
    check = int(input('Enter Any NUmber Between 1 to 100 : '))
    if check == num:
        print('You Win')
        break
    elif check > num:
        print('Guess is Too High')
    else:
        print('guess os Too Low')
else:
    print('You loss ')