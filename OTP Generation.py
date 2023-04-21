# Python Program to Generate an OTP.

import random
# print('Your O T P : ', random.randint(1111, 9999))

'''otp, i = [], 0
while i < 4:
    digit = random.randint(0, 9)
    if digit not in otp:
        otp.append(digit)
        i += 1
else:
    print('Your OTP : ', end = '')
    for num in otp:
        print(num, end=' ')'''

def otp_Generation():
    otp, i = [], 0
    while i < 4:
        digit = random.randint(0, 9)
        if digit not in otp:
            otp.append(digit)
            i += 1
    else:
        return otp
OTP = otp_Generation()
print('Your OTP : ', end= '')
for num in OTP:
    print(num, end= ' ')
