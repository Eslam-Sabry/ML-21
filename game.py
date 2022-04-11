import random
from xmlrpc.client import Boolean


##########global variables#######
cards = [1,2,3,4,5,6,7,8,9,10,11]
random.shuffle(cards)
win_condition = 15
max_value = 21
yes_or_no = {
    'y':True,
    'n':False
}


'''
#######player###############
player_initial_value = cards.pop(0)
player_hand = []
player_hand.append(cards.pop(0))
print(player_initial_value)
print(player_hand)
player_response = input('hit me? type y or n')

while yes_or_no[player_response]:
    player_hand.append(cards.pop(0))
    print(player_initial_value)
    print(player_hand)
    player_response = input('hit me? type y or n')

player_hand_value = sum(player_hand,player_initial_value)
if player_hand_value > win_condition:
    print('you won')
else:
    print('you lost')
'''



#############################################
class Player:
    def __init__(self,name,cards,is_play_first:bool):
        self.initial_value = cards.pop(0)
        self.hand = [cards.pop(0)]
        self.is_player_turn = is_play_first
        self.response = True
        self.name = name
    
    @property
    def hand_value(self):
        return sum(self.hand,self.initial_value)

    def input(self):
        self.response = yes_or_no[input('hit me? type y or n:\n')]
    
    def update_hand(self):
        self.hand.append(cards.pop(0))
    
    def play(self):
        if self.is_player_turn:
            print(f'{self.name} turn')
            print(f'Total value {self.hand_value}')
            print(f'hidden card {self.initial_value}')
            print(f'player hand {self.hand}')
            self.input()
            
            if self.response:
                self.update_hand()
            
            self.is_player_turn = False
        else:
            self.is_player_turn = True


class Stupid_AI(Player):
    def play(self):
        if self.is_player_turn:
            if self.hand_value < 17:
                self.response = True
                self.update_hand()
                print(f'AI hand {self.hand}')
            else:
                self.response = False

            self.is_player_turn = False
        else:
            self.is_player_turn = True


player1 = Player('player1',cards,True)
#player2 = Player('player2',cards,False)
player2 = Stupid_AI('stupid AI',cards,False)


while player1.response or player2.response:
    player1.play()
    player2.play()
    print('########################################')
    if player1.hand_value > max_value or player2.hand_value > max_value:
        break



print(f'{player1.name} hand is {player1.initial_value} + {player1.hand} and the totoal is {player1.hand_value}')
print(f'{player2.name} hand is {player2.initial_value} + {player2.hand} and the totoal is {player2.hand_value}')


if (player1.hand_value > player2.hand_value and player1.hand_value <= max_value) or player2.hand_value > max_value:
    print('player1 wins!')

elif (player2.hand_value > player1.hand_value and player2.hand_value <= max_value) or player1.hand_value > max_value:
    print('player2 wins!')
else:
    print('draw!')