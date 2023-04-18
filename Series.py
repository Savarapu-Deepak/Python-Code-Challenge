# Python Program to print Series.

num = int(input('Enter Range : '))
sum = 0
for i in range(1, num + 1):
    if i < num:
        print('1/{}'.format(i), end=' + ')
    else:
        print('1 / {}'.format(i))
        sum += 1 / i
print(round(sum, 2))