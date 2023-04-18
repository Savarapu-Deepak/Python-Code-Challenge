# Python Program to print Equilateral, Isoscles and Scalene Traingle.

a = float(input('Enter Side 1 : '))
b = float(input('Enter Side 2 : '))
c = float(input('Enter Side 3 : '))

if a == b and b == c:
    print('Triangle is Equilateral Triangle')
elif a == b or b == c or c == a:
    print('Triangle is Isoscles Triangle')
else:
    print('Triangle is Scalene triangle')