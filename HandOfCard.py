import random
class deak:
    type = ['Club','Spde','Dmnd','hrts']
    numbers = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    cards = []
    def __init__(self):
        
        for i in deak.type:
            for j in deak.numbers:
                deak.cards.append(j + ' of ' + i)
        # print(deak.cards)
    def shuffle(self):
        random.shuffle(deak.cards)
        return deak.cards
    remCards = []
    def delCard(self):
        
        print('\nSelect card Type: ')
        for i in deak.type:
            print(i)
        t = int(input())
        ty = deak.type[t-1]
        print('\nSelect card: ')
        for i in deak.numbers:
            print(i)
        c = int(input())
        ca = deak.numbers[c-1]
        rem = ca +' of '+ ty
        deak.cards.remove(rem)
        deak.remCards.append(rem) 
        print(rem,'is Removed!')
    def AddDelCards(self):
        deak.cards = deak.cards + deak.remCards
        print('Cards',deak.remCards,'are added!')
        deak.remCards.clear()
    def hand(self):
        n = int(input('\nEnter size of Hand: '))
        for i in range(n):
            print(deak.cards[random.randint(0,len(deak.cards))])

dk = deak()
def showDeak():
    for j in range(len(dk.cards)):
        print(dk.cards[j],end=",")
        if (j+1)%13 == 0:
            print("\n")
    print("\n-----------------------------------------")
    print('Deleted Cards ',deak.remCards)
    print("-----------------------------------------")

import os
while(True):
    print('\nChoose from the given Options: ')
    ch = int(input(('1. Show Deck \n2. Shuffle the Deck\n3. Delt card \n4. Add Deleated Cards \n5. Show Hand \n6. Exit\n>>')))
    os.system('cls')
    if ch == 1:
        showDeak()
    elif ch == 2:
        dk.shuffle()
    elif ch == 3:
        dk.delCard()
    elif ch == 4:
        dk.AddDelCards()
    elif ch == 5:
        dk.hand()
    else:
        break


    
# print(dk.shuffle())