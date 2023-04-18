# Python Program to print Shopping Bill With Discount Amount.

name = input('Enter Customer Name : ')
cost = float(input('Enter Cost of the Product in Rs: '))
quantity = float(input('Enter Quantity of the Product : '))
bill = cost * quantity
gst = (12/100) * bill
total_Bill = bill + gst
if total_Bill < 1000:
    print('No Discount')
elif total_Bill > 1000 and total_Bill < 3000:
    Discount = (10 / 100) * total_Bill
else:
    Discount = (20 / 100) * total_Bill

print('Amount : ', bill, 'Rupees')
print('GST : ', gst)
print('Discount Amount : ', Discount)
print('Total Amount : ', total_Bill - Discount, 'Rupees Only')