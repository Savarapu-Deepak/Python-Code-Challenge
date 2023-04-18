# Python Program to print Sum of the Digits of a Number.

num = int(input('Enter Any NUmber : '))
sum = 0
while num > 0:
    rem = num % 10
    sum += rem
    num //= 10
else:
    print(sum)