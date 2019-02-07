from random import randint
coin = 39

def game(coin):
	while (coin>0):
		if (coin<=3):
			print("computer turn\n")
			coin = coin - coin
			print("\ncomputer wins")
			break
		else:
			print("computer turn")
			coin = coin - randint(1,3)
			print('coin left:')
			print(coin)
			print('\n')

		if (coin<=3):
			print("Player turn ::  ")
			coin = coin - coin
			print("\nPlayer wins")
			break
		else:
			print("Player turn ::  ")
			coin = coin - int(input())
			print('coin left:')
			print(coin)
			print('\n')
			
game(coin)