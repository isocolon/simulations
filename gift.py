import random
from collections import defaultdict

print()

def PlayGiftGame(players):
	current = 0
	n = players

	received = [False for _ in range(n)]

	while True:
		#print(f'Person {current+1} now has the gift.')
		
		# Check if current player is receiving the gift for the first time
		if not received[current]:
			#print(f'Person {current+1} received the gift for the first time!')
			received[current] = True

		# Check if all players have received the gift
		if all(received) == True:
			#print(f'Person {current+1} was the last person to receive the gift for the first time!')
			#print(f'Person {current+1} is the winner!')						
			return current
		
		# Pass the gift randomly to an adjacent person
		else:			
			direction = random.choice([-1, 1])
			current = (current + direction) % n

results = defaultdict(lambda:0)

for _ in range(1000000):
	results[PlayGiftGame(10)] += 1

print(results)
