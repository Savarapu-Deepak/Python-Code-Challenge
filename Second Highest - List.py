# Python Program to Print Second Highest Number in a List.

'''data = eval(input('Enter List Data : '))
m = max(data)
if m in data:
    data.remove(m)
res = max(data)
print('Second Highest Number : ', res)'''

#Second Highest NUmber in Different Method.

data = eval(input('Enter List Data : '))
max, min = 0, 0
for num in data:
    if num > max:
        max = num
else:
    for num in data:
        if num != max and num > min:
            min = num
    else:
        print('Second Highest NUmber : ', min)

