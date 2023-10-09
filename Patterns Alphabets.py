Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''                                        # print 4 v 4 #
for i in range(4):
    for j in range(4):
        print('#',end=' ')
    print()
'''
'''
for i in range(4):                          # print hollow box
    for j in range(4):
        if i==0 or i==3 or  j==0 or j==3:
            print('#',end=' ')

        else:
            print(' ',end=' ')
    print()
'''
'''
for i in range(4):                           # print u
    for j in range(4):
        if  j==0 or j==3 or i==3:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
for i in range(4):                             # print l
    for j in range(4):
        if j==0 or i==3:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
for i in range(5):                               # print i
    for j in range(5):
        if j==2 or i==0 or i==4:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
for i in range(5):                                # print h
    for j in range(5):
        if i==2 or j ==0 or j== 4:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
for i in range(5):                               # print x
    for j in range(5):
        if i ==0 and j==0 or i==1 and j==1 or i==2 and j==2 or i==3 and j==3 or i==4 and j==4 or i ==0 and j==4 or i==1 and j==3 or i==3 and j==1 or i ==4 and j==0:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
for i in range(4):                               # print z
    for j in range(4):
        if i==0 or i==2 and j==1 or i==1 and j==2 or i==3:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()