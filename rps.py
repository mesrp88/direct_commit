import random
import sys
print("Let's play ROCK PAPER and SCISSOR with computer")
wins=0
lose=0
draw=0
try:
    n= int(input('How many round you wants to play this game: '))
except ValueError:
    print('please enter any integer, not word or symbol')
    n= int(input('How many round you wants to play this game: '))
print('=====================================================')
for i in range(n):
    #taking input from user
    user_input= input('Enter ROCK(R), PAPER(P), SCISSOR(S),  QUIT(Q): ')
    if  user_input=='Q':
        print('You quit, brother->GAME ENDED')
        sys.exit()
    elif user_input=="R":
        print("Rock VS..")
    elif user_input=='P':
        print('Paper VS..')
    elif user_input=='S':
        print('Scissor VS..')

    #randomly generating number and assigning
    comp_inp= random.randint(1,3)
    if comp_inp==1:
        comp_inp='R'
        print("Rock")
    elif comp_inp==2:
        comp_inp="P"
        print('Paper')
    elif comp_inp==3:
        comp_inp='S'
        print("Scissor")
    #checking condition of win , loss,  draw and counting
    if user_input=="R" and comp_inp=='R':
        draw+=1
        print('DRAW')
    elif user_input=="R" and comp_inp=='P':
        lose+=1
        print('YOU LOSS')
    elif  user_input=="R" and comp_inp=='S':
        wins+=1
        print('YOU WIN')
    elif user_input=="P" and  comp_inp=='R':
        wins+=1
        print("YOU WIN")
    elif user_input=='P' and comp_inp=='P':
        draw+=1
        print('DRAW')
    elif user_input=='P' and comp_inp=='S':
        lose+=1
        print('YOU LOSS')
    elif user_input=='S'and  comp_inp=='R':
        lose+=1
        print('YOU LOSS')
    elif user_input=='S'and  comp_inp=='P':
        wins+=1
        print('YOU WIN')
    elif user_input=='S'and  comp_inp=='S':
        draw+=1
        print('DRAW')
    print("==============================================")
print(f'win: {wins}, lose:{lose}, draw:{draw}')
if draw==n and wins==lose:
    print('Final Game is DRAW Between Player')
elif wins>lose:
    print('You win the GAME')
else:
    print('opponent win the Game')





        
        





        
        