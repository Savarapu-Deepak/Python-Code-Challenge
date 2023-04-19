# Cartisean Product.

list_1 = eval(input('Enter List_1 Data : '))
list_2 = eval(input('Enter List_2 Data : '))
result = []
for i in list_1:
    for j in list_2:
        result.append((i, j))
else:
    print(result)
