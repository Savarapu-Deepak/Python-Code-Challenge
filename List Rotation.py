# Python Program to Rotate the List.

list_1 = eval(input('Enter List Data : '))
n = int(input('Enter Position to Rotate : '))

res = list_1[n:] + list_1[:n]
print(res)