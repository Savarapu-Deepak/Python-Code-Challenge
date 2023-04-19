# String Palindrome Check

'''data = input('Enter Any String : ')
if data[::1] == data[::-1]:
    print(data, 'is a Palindrome')
else:
    print('Not a Palindrome')'''

# Second Method

data = input('Enter Any String : ')
res = ''
for char in data:
    res = char + res
else:
    if data == res:
        print('Is a Palindrome')
    else:
        print('Not a Palindrome')

