Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Node:

    def __init__(self,data):
        self.data=data
        self.ref=None

class Linkedlist:

    def __init__(self):
        self.head=None

    def empty(self):
        if self.head is None:
            print('Linked List is Empty !')

        else:
            while n is not None:
                
                                    # self.head.data
                n=n.ref
            n=self.head

L1= Linkedlist(10)
L1.empty()