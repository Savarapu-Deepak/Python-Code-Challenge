# Python Program to Print Leap year or not.

year = int(input('Enter Year : '))
if year % 4 == 0 or year % 400 == 0:
    print(year,' is Leap Year')
else:
    print(year, 'is not a Leap Year')
