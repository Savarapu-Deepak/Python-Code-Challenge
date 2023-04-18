# Python Program to print Prime Numbers with in range.

low = int(input('Enter Lower Value : '))
high = int(input('Enter High Value : '))
if low >= 1:
    for i in range(low, high + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, 'is a Prime Number')

