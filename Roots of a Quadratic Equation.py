# Python Program to Print Roots of a Quadratic Equation.

a = float(input('Enter a Value : '))
b = float(input('Enter b Value : '))
c = float(input('Enter c Value : '))

descriminant = (b ** 2) - 4 * a * c

if descriminant < 0:
    print('There are No Roots')
elif descriminant == 0:
    r1 = r2 = -b / (2 * a)
    print('Roost are : ', r1, r2)
else:
    r1 = (-b + ((b ** 2) - 4 * a * c) ** 0.5) / 2 * a
    r2 = (-b + ((b ** 2) - 4 * a * c) ** 0.5) / 2 * a
    print('Roots are : ', r1, r2)


