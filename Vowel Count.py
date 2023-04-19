# Python Program to Count No.of Vowels in a String.

data = input('Enter Any String Data : ')
check, count = 'AEIOUUaeiou', 0
for char in data:
    if char in check:
        count += 1
else:
    print('No.of.Vowels : ', count)
