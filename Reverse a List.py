# Python Program to Reverse a List.

data = ['Hie', 'True', False, 25.8, 10, 9+8j]
print(data[::-1])
new_data = []

for item in data:
    new_data.insert(0, item)
else:
    print(new_data)