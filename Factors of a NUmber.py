# Python Program to Print factors of a Number.

num = int(input('Factors of the NUmber : '))
print('The Factors of given number {} are : '.format(num))
for i in range(1, num + 1):
    if num % i == 0:
        print(i)