# Python Program to print HCF or GCD of Two Numbers.

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
print(GCD(50, 20))