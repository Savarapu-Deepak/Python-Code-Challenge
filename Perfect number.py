# Python Program to print Perfect Numnber.

num = int(input('Enter Number : '))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
else:
    if num == sum:
        print(num, 'is a Perfect Number')
    else:
        print(num, 'is not a Perfect Number')

