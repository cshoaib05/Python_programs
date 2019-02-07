

import random

cards = ['AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AC','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH']
# S-SPADE D-DIAMOND C-CLUB H-HEART
trump = random.choice(cards)
trump = trump[1:]

print("TRUMP SUIT IS "+trump) # S-SPADE D-DIAMOND C-CLUB H-HEART
winPlayer1 = 0
winPlayer2 = 0
player1cards=0
player2cards=0

def win(player1,player2,trump):
   global winPlayer1,winPlayer2,player2cards,player1cards
   if player1[1:] in player2[1:] or player2[1:] in player1[1:]: # HAVING THE SAME SUIT
       high = higher(player1,player2)                   # CHECKING THE HIGHER CARD
       if high == player1:
           print("player1 Wins")
           winPlayer1 = winPlayer1+1                       # COUNTING THE WINNER OF PLAYERS
           player1cards = player1cards+2       # COUNTING THE PLAYERS CARD
       else:
           print("player2 Wins")
           winPlayer2 = winPlayer2+1
           player2cards = player2cards+2
   elif trump in player1:
       print("player1 Wins")
       winPlayer1 = winPlayer1+1
       player1cards = player1cards+2
   elif trump in player2:
       print("player2 Wins")
       winPlayer2 = winPlayer2+1
       player2cards = player2cards+2
   else:
       print("TIE")

def higher(player1,card2): # HIGHER FUNCTION FOR GETTING HIGHER CARD
   card1 = player1[:1]
   card2 = player2[:1]
   if 'A' in card1:
       card1 = '1'
   if 'A' in card2:
       card2 = '1'

   if 'J' in card1:
       card1 = '11'
   if 'J' in card2:
       card2 = '11'

   if 'Q' in card1:
       card1 = '12'
   if 'Q' in card2:
       card2 = '12'

   if 'K' in card1:
       card1 = '13'
   if 'K' in card2:
       card2 = '13'

   if '0' in card1:
       card1 = '10'
   if '0' in card2:
       card2 = '10'

   if int(card1)==1:
       return player1
   elif int(card2)==1:
       return player2
   elif(int(card1) > int(card2)):
       return player1
   else:
       return player2

while len(cards)!=0:                      # FOR CONTINUE CHOOSING CARDS FROM DECK UNTILL IT FINISH
   player1 = random.choice(cards)
   print("\nplayer 1 card "+player1)
   cards.remove(player1)
   player2 = random.choice(cards)
   cards.remove(player2)
   print("player 2 card "+player2+"\n")
   win(player1,player2,trump)

print("\n\n\nPLAYER 1 WON: "+str(winPlayer1)+" ROUNDS")   # PRINTING THE WINNING ROUNFS AND CARDS
print("PLAYER 2 WON: "+str(winPlayer2)+" ROUNDS")
print("PLAYER 1 HAVE "+str(player1cards)+" CARDS")
print("PLAYER 2 HAVE "+str(player2cards)+" CARDS\n\n\n")

if player1cards > player2cards:   # PRINTING WINNER
   print("WINNER IS PLAYER 1")
else:
   print("WINNER IS PLAYER 2")

# S-SPADE D-DIAMOND C-CLUB H-HEART
# S-SPADE D-DIAMOND C-CLUB H-HEART
# S-SPADE D-DIAMOND C-CLUB H-HEART
