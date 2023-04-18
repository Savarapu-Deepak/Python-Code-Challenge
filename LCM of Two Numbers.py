# Python Program to Print LCM of two NUmbers.

a = int(input('Enter Number 1 : '))
b = int(input('Enter Number 2 : '))
if a > b:
    higher = a
else:
    higher = b
value = higher
while True:
    if higher % a == 0 and higher % b == 0:
        print('LCM of {} and {} is {}'.format(a, b, higher))
        break
    else:
        higher += value


