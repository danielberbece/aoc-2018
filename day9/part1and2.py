from collections import deque

def get_highest_score(num_players, max_marble):
	marbles = deque([0])
	scores = [0 for i in range(num_players + 1)]
	current_player = 1
	marble_to_add = 1
	current_index = 0	# current marble
	for i in range(1, max_marble + 1):
		if i % 23 == 0:
			# Add to score
			scores[current_player] += i
			marbles.rotate(7)
			scores[current_player] += marbles.pop()
			marbles.rotate(-1)
		else:
			# Add marble for current player
			marbles.rotate(-1)
			marbles.append(i)

		current_player += 1
		if(current_player > num_players):
			current_player = 1

	return max(scores)

inputs = [int(x) for x in [line.rstrip('\n') for line in open('in.txt')][0].split()]

print "Part 1: %d"%get_highest_score(inputs[0], inputs[1])
print "Part 2: %d"%get_highest_score(inputs[0], 100 * inputs[1])
