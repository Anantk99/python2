Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
player_wins=0
computer_wins=0

select=['rock','paper','sissor']
p=0

while p<8:
    user=input('rock \ paper \ sissor\ q for quit: ')
    if user == 'q':
        break
    if user not in select:
        continue

    guess= random.randint(0,2)
    computer_pick= select[guess]

    if user== 'rock' and computer_pick == 'paper' :
        computer_wins= computer_wins + 1
        continue
    elif user=='sissor' and computer_pick==' paper':
        print('You Won')
        player_wins=player_wins + 1
        continue
    elif user=='paper' and computer_pick== 'rock':
        print('You Won')
        player_wins=player_wins + 1
        continue
    elif user== 'rock' and computer_pick=='scissor':
        print('You Won')
        player_wins=player_wins + 1
        continue
    else:
        print('Computer Won')
        computer_wins=computer_wins + 1

print('How Many Times You Won',player_wins)
print('How Many Times Computer Won',computer_wins)