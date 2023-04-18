cp = float(input('Enter Cost Price : '))
sp = float(input('Enter Selling Price : '))
if cp > sp:
    print('Loss Amount : ', cp - sp)
elif cp < sp:
    print('Profit Amount : ', sp - cp)
else:
    print('No Profit and No Loss')