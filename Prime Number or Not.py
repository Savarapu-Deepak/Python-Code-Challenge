# Python Program to Check Given Number is Prime or not.

num = int(input('Enter Any Number : '))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, 'not a Prime Number')
            break
    else:
        print(num, 'is a Prime Number')