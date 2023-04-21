# Python Program to print String Swap Case.

data = input('Enter Any String Data : ')
res = ''
for char in data:
    if char.isupper():
        res += char.lower()
    else:
        res += char.upper()
else:
    print(res)