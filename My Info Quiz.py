Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello Lets Play A Quiz Game')

permission= input('Do You Yant To Play Game: ')

if permission.lower() != 'yes':
    quit()
score=0
print('Lets Play Thanks For Play With Me:')

#1
answer = input('Where Is Shreya Mishra ? ')
if answer.lower() == 'jabalpur':
    print('Correct')
    score=score + 1
else:
    print("Wrong")

#2

answer=input('What Is The Biggest Fear Of Mine? ')
if answer.lower()== 'horror movies':
    print('Correct')
    score=score + 1
else:
    print('Wrong')

#3

answer= input('Which Teacher We Call Pirana? ')
if answer.lower() == 'rashmi':
    print('Correct')
    score=score + 1
else:
    print('wrong')

 #4

answer= input('Which Girl Was Victim Of Chalk Incident? ')
if answer.lower()== 'harshita singh':
    print('Correct')
    score=score+1
else:
    ('Wrong')

#5

answer= input('Which Is Our Common Target Class? ')
if answer.lower()== 'ambuj' or 'sourabh':
    print('Correct')
    score=score + 1
else:
    print('Wrong')

#6

answer= input('How Many Dogs Currently I Have? ')
if answer.lower()== '1':
    print('Correct')
    score=score + 1
else:
    print('Wrong')

#7

answer=input('How Many Times I Have Done Kiss ')
if answer.lower()== '0' :
    print('Correct')
    score= score + 1
else:
    print('Wrong')

#8

answer=input('To Which Person I Respect Most (In Friends) ')
if answer.lower()== 'prakhar' :
    print('Correct')
    score= score + 1
else:
    print('Wrong')

#9

answer = input('Do You Like My Phone? ')
if answer.lower() == 'no' :
    print('Correct')
    score = score + 1
else:
    print('Wrong')

#10

answer= input('Which Is More I Prefer 1.Girlfriend 2.Food 3.Partys 4. Money? ')
if answer.lower()== 'money' :
    print('Correct')
    score=score + 1
else:
    print('Wrong')

print('Your Score is', str(((score)/10)*100),'Wow')
