mylist = ['','0','']

from random import shuffle

def go(mylist):
    shuffle(mylist)
    return mylist

def player():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Enter the number 0,1,2 ')
    return int(guess)

def check(mylist,guess):
    if mylist[guess] == '0':
        print('Correct!!')
    else:
        print('Incorrect!!')
        print(mylist)
        
update_list = go(mylist)
guess = player()
check(update_list,guess)
