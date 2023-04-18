# Python Program to print Area and Circumference of a Circle.
'''
Area of a Circle -------> Pi * Radius * Radius
Circumference of a Circle --------->  2 * Pi * Radius.
'''

radius = float(input('Enter Radius of a Circle in cms: '))
pi = 3.14
area = pi * (radius ** 2)
circumference = 2 * pi * radius
print('Area of the Circle is : ', round(area, 3), 'sq.cms')
print('Circumference of the Circle : ', round(circumference, 3), 'cms')