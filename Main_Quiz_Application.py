Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> userdata = {}
username = []
score = 0
def option () :
    choice=input('Enter A Option \n 1.Registration \n 2.Attempt A Quiz \n 3. Display_Result \n 4.Exit \n What you Want :::   ')
    if choice == '1':
        registration()
    elif choice == '2':
        attempt_a_Quiz()
    elif choice == '3':
        Display_Result()
    elif choice == '4':
        exit()
    else:
        print('Enter a Valid Chioce :  ')
        option()
def registration() :
    global userdata
    global username
    print('Register Here First :  ')
    name = input('Enter Your Name :')
    email = input('Enter a Valid Email ID :  ')
    password = input('Enter A Unique Password')
    userdata[name] = [ name , email , password]
    username.append(name)
    print("Registration Successful :  ")
    option()

def attempt_a_Quiz():
    global userdata
    global username
    global score
    name=input('Enter Your Name Please :::  ')
    if name not in username:
        print('Hands Up You Are Not A Part Of us: ')
        registration()
    else:

        ques={1:['Python is?\n 1.high level programing language \n 2. low level programming language \n 3. same as C \n 4.None of these :  '],
              2:['Which of these is not Operator?\n 1./ \n 2. * \n 3._ \n 4. + :  ']
              ,3:['Which is one of this is a keyword\n 1.from \n 2. if \n 3.was \n 4. of :  ']
              ,4:['Which One in Python is mutable? \n 1.strings \n 2. int \n 3. all \n 4. lists: ']
              ,5:['Which one is list function? \n 1.startwith \n 2. isalpha \n 3.split \n 4.reverse: ']}
        ans=[1,3,2,4,4]
        op=0
        for key,val in ques.items():
            print(val[0])
            print(val[1])
            user_ans=input('Enter Your Answer: ')
            if user_ans== ans[op]:
                score=score+1
            print()
            op=op+1
    Display_Result()


def Display_Result():
    global userdata
    global username
    global score
    score=0
    print('Your Score is ',score)
    choice=input('Do You Want To Pkay Again Y \ N  ??? ')
    if choice =='Y'.lower():

        attempt_a_Quiz()
    else:
        exit()
def exit():
    print('Bye Good ')
    exit()
option()