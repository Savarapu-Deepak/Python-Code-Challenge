# Check Number is bInary or Not.

num = int(input('Enter Any Binary Data : '))
while num > 0:
    if num % 10 != 0 or num % 10 != 1:
        print('Not a Binary Number')
        break
    else:
        num = num // 10
    if num == 0:
        print('Is a Binary Number')