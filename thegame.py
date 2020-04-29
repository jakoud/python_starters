from random import randint
import time
print('Hello! Welcome to the game :)\n ')
time.sleep(1)
print('The game is about choosing the right range for random number picked. Players have to score the closest to 21. Whoever surpasses the sum of 21, loses.\n')
time.sleep(2)
print('Be sure to play it with a friend!')
time.sleep(1)
message_entry=input('Would you like to play this game?(yes/no): ')
if message_entry=='yes':
    flag=True
    game='on'
    player_scores=[]
    player_hold=[]
    players=int(input('How many person would like to play?: '))
    while(players<1):
        players=int(input('Give me a proper amount of players, please: '))
    for value in range(0, players):
        player_scores.append(0)
        player_hold.append('no')
else:
    flag=False
while flag:
    for value in range(0, players):
        player_scores[value]=0
        player_hold[value]='no'
    while(game=='on'):
        for value in range(players):
            if player_hold[value]=='yes':
                player_hold[value]=input('Player %d, would you like to still hold?(yes/no): ' %(value+1))
                while(player_hold[value]!='yes' and player_hold[value]!='no'):
                    player_hold[value]=input('Player %d, give me a proper answer: ' %(value+1))
                continue
            else:
                player_range=int(input('Player %d, give me a range: ' %(value+1)))
                player_scores[value]+=randint(1, player_range)
                time.sleep(1)
                print('Player %d, your current score is %d' %((value+1), player_scores[value]))
                
                if(player_scores[value]>21):
                    print('Player %d loses!' %(value+1))
                    game='off'
                    break
                time.sleep(1)
                player_hold[value]=input('Player %d, would you like to hold?(yes/no): ' %(value+1))
                while(player_hold[value]!='yes' and player_hold[value]!='no'):
                    player_hold[value]=input('Player %d, give me a proper answer: ' %(value+1))
                
    winner_position=0
    current_best=0
    for item in player_scores:
        if (item<=21 and item>current_best):
            current_best=item
            winner_position+=1
    
    if winner_position==0:
        print('No one wins :(')
    else:    
        print('Player %d wins!' %winner_position)

    message_out=input('Would you like to play again?(yes/no): ')
    if message_out=='no':
        flag=False

print('\nThank you for your time :)')