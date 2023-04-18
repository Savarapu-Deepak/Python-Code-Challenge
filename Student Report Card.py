# Print Student Report Card.

name = input('Enter Student Name : ')
English = int(input('Enter Marks in English : '))
Maths = int(input('Enter Marks in Maths : '))
Science = int(input('Enter Marks in Science : '))
Social = int(input('Enter Marks in Social : '))
Telugu = int(input('Enter Marks in Telugu : '))
Hindi = int(input('Enter Marks in Hindi : '))
Total = English + Maths + Science + Social + Telugu + Hindi
Percentage = round((Total / 600) * 100, 2)
print('-' * 25)
print(name, 'Report Card')
print('-' * 25)
print('Total Marks out of 600 : ', Total)
print('Overall Percentage : ', Percentage, '%')

if Percentage >= 40 and Percentage <= 50:
    print('Congratulations, You Passed The Exam..')
elif Percentage >= 51 and Percentage <= 60:
    print('Congratulations, Your Performance is Average')
elif Percentage >= 61 and Percentage <= 70:
    print('Congratulations, Your Performance is Good')
elif Percentage >= 71 and Percentage <= 80:
    print('Congratulations, Your Performance is Better')
elif Percentage >= 81 and Percentage <= 90:
    print('Congratulations, Your Performance is Best.')
elif Percentage >= 91 and Percentage <= 100:
    print('Congratulations, Your Performance is Excellent')
else:
    print('Sorry, Better Luck In Next Semester')