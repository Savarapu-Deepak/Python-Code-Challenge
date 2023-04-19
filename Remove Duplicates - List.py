# Python Program to Remove Duplicates in a List.

data = eval(input('Enter List Data : '))
new_data = []
for item in data:
    if item not in new_data:
        new_data.append(item)
else:
    print(new_data)