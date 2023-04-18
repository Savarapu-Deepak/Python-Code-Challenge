# Python Program to print Multiplication of a Table.

num = int(input('Enter Number : '))
for i in range(1, 13):
    print('{} X {} = {}'.format(num, i, (num * i)))
else:
    print('Task Completed.')