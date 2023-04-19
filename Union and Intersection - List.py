# Python Program to Print Union and Intersection Between Two Lists.

data_1 = eval(input('Enter List Data_1 : '))
data_2 = eval(input('Enter List Data_2 : '))

print('Union of Two Lists : ')
for num in data_2:
    if num not in data_1:
        data_1.append(num)
else:
    print(data_1)
print('Intersection of Two Lists : ')
for nums in data_1:
    if nums in data_2:
        print(nums)