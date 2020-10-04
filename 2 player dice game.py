from playsound import playsound
from time import sleep
import random
n=4
print('Welcome to Roll The Dice')
player1 = input("Enter your name Player1: ")
player2 = input("Enter your name Player2: ")
def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return player1
    else:
        return player2

turn = choose_first()
print(turn + ' will go first')

while n>0:
     n-=1
     if n==2:
    
        continue
die1 = random.randint(1,6)
die2 = random.randint(1,6)
playsound('Shake And Roll Dice.wav')
print("The dice rolled and player1 and player2 got: ", die1,die2,sep='\n')
    
print("calculating results\n.\n.\n.")       
    
for i in range(1):
         
        if die1>die2:
             print(f'{player1} is the winner! \U0001F3C6') #f-string, emoji unicode
        elif die1==die2:
             print("It's a draw!")
        else: 
             print(f'{player2} is the winner! \U0001F3C6')
              
        sleep(2)                                #hault the flow of code for any period of time(2sec)
playsound('applause.wav')
         
      
    