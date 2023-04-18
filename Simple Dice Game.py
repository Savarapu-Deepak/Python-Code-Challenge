# Python Program to Print a Simple Dice Game.

import random

player_1 = input('Player_1 : ')
player_2 = input('Player_2 : ')

val_1 = random.randint(1, 6)
val_2 = random.randint(1, 6)

print(player_1, 'throws : ', val_1)
print(player_2, 'throws : ', val_2)

if val_1 > val_2:
    print(player_1, 'Wins')
elif val_2 > val_1:
    print(player_2, 'Wins')
else:
    print('Tie')
