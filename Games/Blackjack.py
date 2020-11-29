'''
This is the code for a simplified blackjack game between a user and the computer.
'''

def blackjack():
	import random
	# allows computer to deal random cards
	import time
	# makes computer wait between turns so game is more realistic

	numbers = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
	# all possible numbers
	suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
	# all possible suits
	deck = [[x,y] for x in numbers for y in suits]
	# all possible cards in deck
	possibilities = [x for x in range(0, 52)]
	# ensures the same card will not be drawn again
	replay = True
	# if replay = False, player does not want to play again
	computer_turn = True
	# it is only the computer's turn if player chooses to stand
	easy_win = True
	# checks to see if player is dealt a perfect 21 on the first hand
	wins = 0
	# keeps track of player's wins
	losses = 0
	# keeps track of player's losses

	class BettingAmount():
		# tracks how much money player has
		def __init__(self, amount):
			self.amount = amount
		def deposit(self, dep_amount):
			# adds money to account
			self.amount += dep_amount
		def withdraw(self, take_amount):
			# takes away money from account
			self.amount -= take_amount


	class Hand():
		# randomly assigns dealer and player two cards
		def __init__(self, player):
			# specifies dealer or player
			self.player = player
		def random_hand(self, repeat):
			# returns number of random cards from deck list designated by repeat
			return_cards = []
			for i in range(0, repeat):
				random_card = random.choice(possibilities)
				possibilities.remove(random_card)
				# removes number from possibilities list so card will not be chosen again
				return_cards.append(deck[random_card])
			return return_cards


	def sum(persons_cards):
		# finds sum of values of cards
		def value(number):
			# gives a value to the card
			if number == 'Ten' or number == 'King' or number == 'Queen' or number == 'Jack':
				return 10
			elif number == 'Ace':
				return 11
			else:
				return numbers.index(number) + 1
		card_sum = 0
		count = 0
		# count keeps track of index of persons_cards
		for i in persons_cards:
			# adds up values of all cards
			card_sum += value(persons_cards[count][0])
			count += 1
		count = 0
		for i in persons_cards:
			# if player or dealer has ace and exceeds 21 the ace earns a value of 1 instead of 11
			if card_sum > 21:
				if persons_cards[count][0] == 'Ace':
					card_sum -= 10
					count += 1
			else:
				break
		return card_sum


	def card_name(card_in_deck):
		# converts number/suit pair into phrase (ex: 'Ace of Hearts')
		card_phrase = ''
		for i in card_in_deck:
			card_phrase += f'\n{i[0]} of {i[1]}'
		return card_phrase


	def leave(l_input):
		# checks to see if player wants to leave the game
		cap_input = l_input.upper()
		if cap_input == 'LEAVE' or cap_input == 'EXIT' or cap_input == 'L' or cap_input == 'E':
			return False


	def move(move_input):
		# checks to see if player wants to hit or stand
		cap_move_input = move_input.upper()
		if cap_move_input == 'HIT' or cap_move_input == 'H':
			# checks to see if player is within 21 point limit
			if (sum(player_cards)) == 21:
				return 'win'
			elif (sum(player_cards)) > 21:
				return 'lose'
			elif (sum(player_cards)) < 21:
				return True
		elif cap_move_input == 'STAND' or cap_move_input == 'S':
			return False

	# gameplay starts here

	print('\nWelcome to BLACKJACK!!\nGet closer to 21 than the dealer without going over!\nYou will start with 2 cards while the dealer has one card shown and one card hidden.\nIf you hit, you will draw another card, but if you stand your turn is over.\nThe dealer will hit until she beats your score or exceeds 21.\nAces count as either 1 or 11, whichever is more preferable.\nYou will start with $500 and can choose how much you want to bet before each round.\nIf you run out of money, you lose the game, but if you earn more than $5000, you beat the game!\nIf you ever want to leave the game, enter (l)eave or (e)xit.\nHave fun!!')
	# prints rules of game
	bank = BettingAmount(500)
	# starts player with $500

	while replay == True:
		# game keeps restarting unless player chooses otherwise
		deck = [[x,y] for x in numbers for y in suits]
		# all possible cards in deck
		possibilities = [x for x in range(0,52)]
		# ensures the same card will not be drawn again
		print(f'\nYou have ${bank.amount} in your bank account.\n')
		# tells player how much money he has
		while True:
			# checks how much money player wants to bet and ensures bet is an integer
			try:
				bet_input = input('How much do you want to bet? $')
				if leave(bet_input) == False:
					print('You are leaving the game.')
					print('\nThank you for playing BLACKJACK!\n')
					break
				elif int(bet_input) <= 0:
					# makes sure bet is not 0 or a negative number
					print('You must bet more than 0 dollars.')
				elif int(bet_input) <= bank.amount:
					# makes sure bet is not more than amount in bank
					bet = int(bet_input)
					break
				else:
					print(f'\nYou can not bet ${bet_input} since you only have ${bank.amount} in your bank account.\n')
			except:
				print('\nPlease input an integer amount for your bet.\n')
				continue
		if leave(bet_input) == False:
			break

		player = Hand('player')
		player_cards = player.random_hand(2)
		print(f"\nPLAYER'S CARDS:{card_name(player_cards)}\nPLAYER SUM: {str(sum(player_cards))}")
		# deals player's first two cards
		dealer = Hand('dealer')
		dealer_cards = dealer.random_hand(1)
		print(f"\nDEALER'S CARDS:{card_name(dealer_cards)}\n<hidden card>\nDEALER SUM: {str(sum(dealer_cards))}")
		# deals dealer's first card
		
		if sum(player_cards) == 21:
			# if the player is immediately dealt a pair that adds up to 21, they automatically win
			print('\nYour hand is worth exactly 21 points, so YOU HAVE WON THIS ROUND!!')
			bank.deposit(bet)
			print(f'YOUR NEW BETTING AMOUNT: ${bank.amount}\n')
			computer_turn = False
			wins += 1
			easy_win = False

		while easy_win == True:
			# asks if player wants to hit or stand
			input1 = input('\nDo you want to (H)IT or (S)TAND? ')
			if leave(input1) == False:
				print('You are leaving the game.')
				print('\nThank you for playing BLACKJACK!\n')
				computer_turn = False
				replay = False
				break
			elif move(input1) == True or move(input1) == 'win' or move(input1) == 'lose':
				# adds a card to player's hand if he chooses to hit if he has less than 21 points
				print('\nYou have chosen to HIT.')
				player_cards.append(player.random_hand(1)[0])
				print(f"\nPLAYER'S CARDS:{card_name(player_cards)}\nPLAYER SUM: {str(sum(player_cards))}\n\nDEALER'S CARDS:{card_name(dealer_cards)}\n<hidden card>\nDEALER SUM: {str(sum(dealer_cards))}")
				if move(input1) == 'win':
					print('You have exactly 21 points!\nYOU HAVE WON THIS ROUND!!\n')
					bank.deposit(bet)
					print(f'YOUR NEW BETTING AMOUNT: ${bank.amount}')
					computer_turn = False
					wins += 1
					break
				elif move(input1) == 'lose':
					print('\nYou have over 21 points!\nYOU HAVE LOST THIS ROUND!!\n')
					bank.withdraw(bet)
					print(f'YOUR NEW BETTING AMOUNT: ${bank.amount}')
					computer_turn = False
					losses += 1
					break
			elif move(input1) == False:
				# ends player's move
				print('\nYou have chosen to STAND.')
				print(f"\nPLAYER'S CARDS:{card_name(player_cards)}\nPLAYER SUM: {str(sum(player_cards))}\n\nDEALER'S CARDS:{card_name(dealer_cards)}\n<hidden card>\nDEALER SUM: {str(sum(dealer_cards))}")
				computer_turn = True
				break

		if computer_turn == True:
			# plays the computer's turn- the computer keeps hitting until the dealer's score is higher than the player's score
			print("Now, it's the computer's turn.")
			time.sleep(1)
			while True:
				if sum(dealer_cards) < sum(player_cards):
					# dealer only hits if his sum is less than the player's sum
					dealer_cards.append(dealer.random_hand(1)[0])
					time.sleep(2)
					print('\nThe dealer has chosen to HIT.')
					print(f"\nPLAYER'S CARDS:{card_name(player_cards)}\nPLAYER SUM: {str(sum(player_cards))}\n\nDEALER'S CARDS:{card_name(dealer_cards)}\nDEALER SUM: {str(sum(dealer_cards))}")
				if sum(dealer_cards) > sum(player_cards):
					break
			if sum(dealer_cards) > sum(player_cards) and sum(dealer_cards) <= 21:
				# the dealer wins if he exceeds the player's sum without exceeding 21
				print('\nTHE DEALER HAS WON THIS ROUND!\n')
				bank.withdraw(bet)
				print(f'YOUR NEW BETTING AMOUNT: ${bank.amount}')
				losses += 1
			elif sum(dealer_cards) > 21:
				# the dealer loses if he exceeds 21
				print('\nThe dealer has exceeded 21. YOU HAVE WON THIS ROUND!!\n')
				bank.deposit(bet)
				print(f'YOUR NEW BETTING AMOUNT: ${bank.amount}')
				wins += 1

		if bank.amount == 0:
			# if player has no more money, he loses the game; if he has more than $5000, he beats the game
			print('\nYou have no more money in your bank account! YOU HAVE LOST BLACKJACK.\n')
			break
		elif bank.amount >= 5000:
			print('\nYou have earned $5000 or more! YOU HAVE WON BLACKJACK!!\n')
			break

		if replay == True:
			# checks if player wants to play again
			print(f'You have {str(wins)} wins and {str(losses)} losses so far!')
			while True:
				try:
					replay_input = input('\nDo you want to play again? ((Y)es or (N)o) ')
					if leave(replay_input) == False:
						print('You are leaving the game.')
						print('\nThank you for playing BLACKJACK!\n')
						break
					elif replay_input.upper() == 'Y' or replay_input.upper() == 'YES':
						replay = True
					elif replay_input.upper() == 'N' or replay_input.upper() == 'NO':
						print('\nThank you for playing BLACKJACK!\n')
						break
					else:
						# force an error
						return 'a' + 1
					break
				except:
					print('\nPlease answer (Y)es or (N)o.\n')
					continue



if __name__ == '__main__':
	# code only runs if file is not imported
	blackjack()
