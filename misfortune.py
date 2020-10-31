import random

def spin():
	return random.choice([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])


def play_player(strategy):
	score = spin()
	
	if score <= 30:
		score += spin()
		if score > 50:
			return -1
		else:
			return score
	elif score < strategy: # score is in [35, 40, 45, 50]
		score += spin()
		if score > 50:
			return -1
		else:
			return score

	return score


def play_house(player_score):
	if player_score == -1:
		return 50

	score = spin()
	if score > player_score:
		return score
	else:
		score += spin()
		if score > 50:
			return -1
		else:
			return score



print('\nStrategy\t\t\t\t\t\tWin Rate')
print('='*40)

SIMULATIONS = 100000

for strategy in [35, 40, 45, 50, 55]:
	player_wins = 0

	for _ in range(SIMULATIONS):
		player_score = play_player(strategy)
		house_score = play_house(player_score)

		if player_score >= house_score:
			player_wins += 1

	winrate = player_wins / SIMULATIONS * 100
	print(f'Spin again if less than {strategy}\t\t{winrate:.2f}%')