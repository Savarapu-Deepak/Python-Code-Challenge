# Python Program to print Factorial Using Recursion.

def Factorial(n):
    if n in [0, 1]:
        return 1
    else:
        return n * Factorial(n-1)
n = int(input('Enter Factorial of a Number : '))
print(Factorial(n))