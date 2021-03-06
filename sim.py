import json
import random

def load_cards():
	cards_json_file = 'AllSets.json'
	json_data=open(cards_json_file).read()
	data = json.loads(json_data)
	return data

def make_deck():
	# just use basic set for now
	card_data = load_cards()['Basic'] 
	deck = list() 
	while len(deck) < 30:
		rand_card = card_data[random.randint(0,len(card_data)-1)]
		# TODO limit max 2 per deck, restrict cards per hero class
		# make smarter choices
		deck.append(rand_card)
	return deck

def draw_card(deck):
	idx = random.randint(0,len(deck)-1)
	rand_card = deck[idx]
	deck.pop(idx)
	return rand_card, deck


def main():
	deck = dict()
	deck['A'] = make_deck()
	deck['B'] = make_deck()
	players = {'A': {'life':20, 'card_count':30, 'turn':0, 'card_penalty':0, 'board_state':{}}, 
			   'B': {'life':20, 'card_count':30, 'turn':0, 'card_penalty':0, 'board_state':{}}}
	turn = 0

	current_player= 'A' if random.randint(1,2) == 1 else 'B'
	# make decks

	while True:
		players[current_player]['turn'] += 1
		players[current_player]['card_count'] += -1
		mana = players[current_player]['turn']

		if mana > 10:
			mana = 10
		print current_player + '\'s turn: ' + str(players[current_player]['turn']) + ', mana: ' + str(mana)

		# draw card, update deck
		if len(deck[current_player]) > 0:
			card, new_deck = draw_card(deck[current_player])
			print 'DRAW CARD'
			print card
			deck[current_player] = new_deck
		else:
			print 'Player ' + current_player + ' out of cards! Lose ' + str(players[current_player]['card_penalty']) + ' life'
			players[current_player]['life'] += -1 * players[current_player]['card_penalty']
			players[current_player]['card_penalty'] += 1

		if 'cost' in card and card['cost'] < mana:
			print 'PLAY CARD'

		# win condition
		if players['A']['life'] <= 0:
			print 'player B wins'
			break
		if players['B']['life'] <= 0:
			print 'player A wins'
			break
		next_player = 'B' if current_player == 'A' else 'A'
		current_player = next_player


if __name__=='__main__':
	main()