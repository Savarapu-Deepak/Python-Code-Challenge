# Python Program to check whether number is palindrome or not.

num = int(input('Enter Any Number : '))
rev, check = 0, num
while num > 0:
    rem = num % 10
    rev = (rev * 10) + rem
    num //= 10
else:
    if check == rev:
        print('Number is a Palindrome Number')
    else:
        print('Number is not a Palindrome Number')
