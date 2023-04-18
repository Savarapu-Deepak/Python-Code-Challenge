# Python Program to print Factorial of a Number.

'''num = int(input('Enter Factorial of a NUmber : '))
res = 1
for i in range(1, num + 1):
    res *= i
else:
    print(res)'''

# In the Reverse Order.

num = int(input('Enter Factorial of a Number : '))
res = 1
for i in range(num, 0, -1):
    res *= i
else:
    print(res)