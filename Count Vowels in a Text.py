# Python Program to Count Vowels in a Given Text.

text = open('story.txt', 'w')
text.write('This is a Sample File Which We are Creating Using Python Program.\n')
text.write('This File will be used through another program to process its Data.\n')
text.write('Thank You.')
text.close()

file = open('story.txt', 'r')
data = file.read()
print(data)
vowels, consonants = 0, 0
for char in data:
    if char in 'AEIOUaeiou':
        vowels += 1
    else:
        consonants += 1
else:
    print('Vowels Count : ', vowels)
    print('Consonants Count : ', consonants)
file.close()