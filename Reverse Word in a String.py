# Python Program to Reverse A Word In A String.

data = input('Enter Any String Data with More Words : ')
res, new_data = data.split(), []
for item in res:
    new_data.insert(0, item)

else:
    result = ' '.join(new_data)
    print(result)

