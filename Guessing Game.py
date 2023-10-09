Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
answer= random.randrange(4,7,2)
chance=0
while chance<3:
    guess= int(input('Enter A number :  ' ))
    if guess == answer:
        print('Right')
        break
    elif guess<answer:
        print('Too Low')
    elif guess> answer:
        print('Too High')
    chance=chance + 1
    