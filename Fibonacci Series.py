# Python Program to Print Fibanocci Series

num = int(input('Enter Fibonacci Range : '))
n1, n2 = 0, 1
while num > 0:
    print(n1, end=' ')
    next_Element = n1 + n2
    n1 = n2
    n2 = next_Element
    num -= 1