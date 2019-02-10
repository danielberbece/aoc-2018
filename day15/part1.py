def attack(dict1, i, j, table, attack_power):
	enemy = dict1[table[i][j]]
	enemy -= attack_power
	dict1[table[i][j]] = enemy
	if enemy < 1:
		del dict1[table[i][j]]
		table[i][j] = '.'
		return 1
	return 0

def check_loc(enemy_type, x, y, table):
	if table[y][x] == '.':
		return 0
	if not isinstance(table[y][x], str) and table[y][x] < 200 and enemy_type == 0:
		return 1
	if not isinstance(table[y][x], str) and table[y][x] > 199 and enemy_type == 1:
		return 1
	return -1
	
def find_closest(enemy_type, x, y, table):
	# 0 for finding goblin, 1 for finding elf
	visited = [[0 for x in row] for row in table]
	Q = [(y, x, [0])]
	visited[y][x] = 1
	found = 0
	while len(Q) > 0:
		pos = Q[0]
		Q.pop(0)
		# print(pos)
		# up
		if visited[pos[0]-1][pos[1]] == 0:
			l = check_loc(enemy_type, pos[1], pos[0]-1, table)			
			visited[pos[0]-1][pos[1]] = 1
			if l == 0:
				dirs = pos[2][:]
				dirs.append(0)
				Q.append((pos[0]-1, pos[1], dirs))
			elif l == 1:
				return pos[1], pos[0], pos[2]
		# left
		if visited[pos[0]][pos[1]-1] == 0:
			l = check_loc(enemy_type, pos[1]-1, pos[0], table)			
			visited[pos[0]][pos[1]-1] = 1
			if l == 0:
				dirs = pos[2][:]
				dirs.append(1)
				Q.append((pos[0], pos[1]-1, dirs))
			elif l == 1:
				return pos[1], pos[0], pos[2]
		# right
		if visited[pos[0]][pos[1]+1] == 0:
			l = check_loc(enemy_type, pos[1]+1, pos[0], table)			
			visited[pos[0]][pos[1]+1] = 1
			if l == 0:
				dirs = pos[2][:]
				dirs.append(2)
				Q.append((pos[0], pos[1]+1, dirs))
			elif l == 1:
				return pos[1], pos[0], pos[2]
		# down
		if visited[pos[0]+1][pos[1]] == 0:
			l = check_loc(enemy_type, pos[1], pos[0]+1, table)			
			visited[pos[0]+1][pos[1]] = 1
			if l == 0:
				dirs = pos[2][:]
				dirs.append(3)
				Q.append((pos[0]+1, pos[1], dirs))
			elif l == 1:
				return pos[1], pos[0], pos[2]
	return -1, -1, [0,-1]


table = [[x for x in line.rstrip('\n')] for line in open("in.txt")]
goblin_ids = 100
elf_ids = 200
elfs = {}
goblins = {}
for i in range(len(table)):
	for j in range(len(table[i])):
		if table[i][j] == 'G':
			table[i][j] = goblin_ids
			goblins[goblin_ids] = 200
			goblin_ids += 1
		elif table[i][j] == 'E':
			table[i][j] = elf_ids
			elfs[elf_ids] = 200
			elf_ids += 1

elf_attack_power = 3
elf_won = 0
copy_table = [row[:] for row in table]
copy_elfs = elfs.copy()
copy_goblins = goblins.copy()
steps = 0

while elf_won == 0:
	table = [row[:] for row in copy_table]
	elfs = copy_elfs.copy()
	goblins = copy_goblins.copy()
	elf_attack_power += 1
	steps = 0
	winner = -1
	elf_won = 1
	while winner == -1:
		steps += 1

		#do a round:
		moved = []
		
		for i in range(len(table)):
			for j in range(len(table[i])):
				if table[i][j] != '.' and table[i][j] != '#':
					#if goblin:
					pos = (0,0)
					mini = 999
					if table[i][j] < 200:
						# take turn
						if not table[i][j] in moved:
							if len(elfs) == 0:
								winner = 1
								break
							moved.append(table[i][j])
							_, _, direction = find_closest(1, j, i, table)
							current_pos = (i, j)
							if len(direction) > 1:
								if direction[1] == -1:
									#no move available
									pass
								elif direction[1] == 0:	#up
									table[i-1][j] = table[i][j]
									current_pos = (i-1, j)
									table[i][j] = '.'
								elif direction[1] == 1:	#left
									current_pos = (i, j-1)
									table[i][j-1] = table[i][j]
									table[i][j] = '.'
								elif direction[1] == 2:	#right
									current_pos = (i, j+1)
									table[i][j+1] = table[i][j]
									table[i][j] = '.'
								elif direction[1] == 3:	#down
									current_pos = (i+1, j)
									table[i+1][j] = table[i][j]
									table[i][j] = '.'	
							if not isinstance(table[current_pos[0]-1][current_pos[1]], str) and table[current_pos[0]-1][current_pos[1]] >= 200:
								if mini > elfs[table[current_pos[0]-1][current_pos[1]]]:
									mini = elfs[table[current_pos[0]-1][current_pos[1]]]
									pos = (current_pos[0]-1,current_pos[1])
							if not isinstance(table[current_pos[0]][current_pos[1]-1], str) and table[current_pos[0]][current_pos[1]-1] >= 200:
								if mini > elfs[table[current_pos[0]][current_pos[1]-1]]:
									mini = elfs[table[current_pos[0]][current_pos[1]-1]]
									pos = (current_pos[0],current_pos[1]-1)
							if not isinstance(table[current_pos[0]][current_pos[1]+1], str) and table[current_pos[0]][current_pos[1]+1] >= 200:
								if mini > elfs[table[current_pos[0]][current_pos[1]+1]]:
									mini = elfs[table[current_pos[0]][current_pos[1]+1]]
									pos = (current_pos[0],current_pos[1]+1)
							if not isinstance(table[current_pos[0]+1][current_pos[1]], str) and table[current_pos[0]+1][current_pos[1]] >= 200:
								if mini > elfs[table[current_pos[0]+1][current_pos[1]]]:
									mini = elfs[table[current_pos[0]+1][current_pos[1]]]
									pos = (current_pos[0]+1,current_pos[1])
							if mini != 999:
								died = attack(elfs, pos[0], pos[1], table, 3)
								if died == 1:
									elf_won = 0

					else:	# elf							
						# move
						if not table[i][j] in moved:
							_, _, direction = find_closest(0, j, i, table)
							moved.append(table[i][j])
							if len(goblins) == 0:
								winner = 0
								break
							# print(direction)
							current_pos = (i, j)
							if len(direction) > 1:
								if direction[1] == -1:
									#no move available
									pass
								elif direction[1] == 0:	#up
									current_pos = (i-1, j)
									table[i-1][j] = table[i][j]
									table[i][j] = '.'
								elif direction[1] == 1:	#left
									current_pos = (i, j-1)
									table[i][j-1] = table[i][j]
									table[i][j] = '.'
								elif direction[1] == 2:	#right
									current_pos = (i, j+1)
									table[i][j+1] = table[i][j]
									table[i][j] = '.'
								elif direction[1] == 3:	#down
									current_pos = (i+1, j)
									table[i+1][j] = table[i][j]
									table[i][j] = '.'
							if not isinstance(table[current_pos[0]-1][current_pos[1]], str) and table[current_pos[0]-1][current_pos[1]] < 200:
								if mini > goblins[table[current_pos[0]-1][current_pos[1]]]:
									mini = goblins[table[current_pos[0]-1][current_pos[1]]]
									pos = (current_pos[0]-1,current_pos[1])
							if not isinstance(table[current_pos[0]][current_pos[1]-1], str) and table[current_pos[0]][current_pos[1]-1] < 200:
								if mini > goblins[table[current_pos[0]][current_pos[1]-1]]:
									mini = goblins[table[current_pos[0]][current_pos[1]-1]]
									pos = (current_pos[0],current_pos[1]-1)
							if not isinstance(table[current_pos[0]][current_pos[1]+1], str) and table[current_pos[0]][current_pos[1]+1] < 200:
								if mini > goblins[table[current_pos[0]][current_pos[1]+1]]:
									mini = goblins[table[current_pos[0]][current_pos[1]+1]]
									pos = (current_pos[0],current_pos[1]+1)
							if not isinstance(table[current_pos[0]+1][current_pos[1]], str) and table[current_pos[0]+1][current_pos[1]] < 200:
								if mini > goblins[table[current_pos[0]+1][current_pos[1]]]:
									mini = goblins[table[current_pos[0]+1][current_pos[1]]]
									pos = (current_pos[0]+1,current_pos[1])
							if mini != 999:
								attack(goblins, pos[0], pos[1], table, elf_attack_power)

total = 0
if winner == 1:	#goblin won
	for x in goblins:
		total += goblins[x]
else:
	for x in elfs:
		total += elfs[x]
print("Answer for part 2 is %d"%(total * (steps-1)))