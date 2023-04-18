# Pattern Printing.
'''
*
* *
* * *
* * * *
* * * * *
'''

rows = int(input('Enter No.of.Rows : '))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end=' ')
    print()

# Pattern in the Reverse Form.
rows = int(input('Enter No.of Rows : '))
for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(chr(64 + j), end=' ')
    print()

