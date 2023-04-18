# Python Program to print Armstrong with in a Range.

'''num = int(input('Enter Any NUmber : '))
sum, check, length = 0, num, len(str(num))
while num > 0:
    rem = num % 10
    sum = sum + (rem ** length)
    num //= 10
else:
    if sum == check:
        print(check, 'is an Armstrong Number')
    else:
        print(check, 'is not an Armstrong NUmber')'''

low = int(input('Enter Lower Value : '))
high = int(input('Enter Higher Value : '))
for i in range(low, high + 1):
    sum, check, length = 0, i, len(str(i))
    while i > 0:
        rem = i % 10
        sum = sum + (rem ** length)
        i //= 10
    else:
        if check == sum:
            print(sum, 'is an Armstrong Number')




