# Python 3 implementation, takes ~15s to run
def part1(inp):
	Q = [3,7]
	elf1_pos = 0
	elf2_pos = 1

	steps = int(inp)

	while len(Q) < steps + 10:
		#make recipe
		new_recipe_value = Q[elf1_pos] + Q[elf2_pos]
		new_recipes = []
		if new_recipe_value > 9:
			Q.append(1)
		Q.append(new_recipe_value % 10)
		elf1_pos += Q[elf1_pos] + 1
		elf1_pos %= len(Q)
		elf2_pos += Q[elf2_pos] + 1
		elf2_pos %= len(Q)

	return ''.join([str(x) for x in Q[steps:steps + 10]])

def part2(inp):
	seq = [int(x) for x in inp]
	Q = [3,7]
	elf1_pos = 0
	elf2_pos = 1

	while True:
		#make recipe
		new_recipe_value = Q[elf1_pos] + Q[elf2_pos]
		new_recipes = []
		if new_recipe_value > 9:
			Q.append(1)
			if len(Q) >= len(seq) and Q[len(Q) - len(seq):] == seq:
				break
		Q.append(new_recipe_value % 10)
		if len(Q) >= len(seq) and Q[len(Q) - len(seq):] == seq:
			break
		elf1_pos += Q[elf1_pos] + 1
		elf1_pos %= len(Q)
		elf2_pos += Q[elf2_pos] + 1
		elf2_pos %= len(Q)

	return len(Q) - len(seq)

aoc_input = '074501'
print(part1(aoc_input))
print(part2(aoc_input))

