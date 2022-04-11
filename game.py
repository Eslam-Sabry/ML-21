import random


##########global variables#######
cards = [1,2,3,4,5,6,7,8,9,10,11]
random.shuffle(cards)
win_condition = 17
yes_or_no = {
    'y':True,
    'n':False
}


#######player###############
player_initial_value = cards.pop(0)
player_hand = []
player_hand.append(cards.pop(0))
player_response = input('hit me? type y or n')

while yes_or_no[player_response]:
    player_hand.append(cards.pop(0))
    player_response = input('hit me? type y or n')

player_hand_value = sum(player_hand,player_initial_value)
if player_hand_value > win_condition:
    print('you won')
else:
    print('you lost')