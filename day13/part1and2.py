grid_system = [[x for x in line.rstrip('\n')] for line in open("in.txt")]
carts = []
ids = 0
for i in range(len(grid_system)):
	for j in range(len(grid_system[0])):
		if grid_system[i][j] == '>':
			grid_system[i][j] = '-'
			carts.append([i, j, 'R', 0, ids])
			ids += 1

		if grid_system[i][j] == '<':
			grid_system[i][j] = '-'
			carts.append([i, j, 'L', 0, ids])
			ids += 1

		if grid_system[i][j] == 'v':
			grid_system[i][j] = '|'
			carts.append([i, j, 'D', 0, ids])
			ids += 1

		if grid_system[i][j] == '^':
			grid_system[i][j] = '|'
			carts.append([i, j, 'U', 0, ids])
			ids += 1

collision = 0
collisions = []
carts_down = []
first_collision = []
while len([c for c in carts if not c[4] in carts_down]) != 1:
	carts.sort()
	for i in range(len(carts)):
		if not carts[i][4] in carts_down:
			cart = carts[i]
			if cart[2] == 'R':
				cart[1] += 1
			elif cart[2] == 'U':
				cart[0] -= 1
			elif cart[2] == 'L':
				cart[1] -= 1
			else:
				cart[0] += 1

			if grid_system[cart[0]][cart[1]] == '/':
				if cart[2] == 'R':
					cart[2] = 'U'
				elif cart[2] == 'U':
					cart[2] = 'R'
				elif cart[2] == 'L':
					cart[2] = 'D'
				else:
					cart[2] = 'L'

			if grid_system[cart[0]][cart[1]] == '\\':
				if cart[2] == 'R':
					cart[2] = 'D'
				elif cart[2] == 'U':
					cart[2] = 'L'
				elif cart[2] == 'L':
					cart[2] = 'U'
				else:
					cart[2] = 'R'

			if grid_system[cart[0]][cart[1]] == '+':
				if cart[3] == 0:
					if cart[2] == 'R':
						cart[2] = 'U'
					elif cart[2] == 'U':
						cart[2] = 'L'
					elif cart[2] == 'L':
						cart[2] = 'D'
					else:
						cart[2] = 'R'
					cart[3] = 1
				elif cart[3] == 1:
					cart[3] = 2
				else:
					if cart[2] == 'R':
						cart[2] = 'D'
					elif cart[2] == 'U':
						cart[2] = 'R'
					elif cart[2] == 'L':
						cart[2] = 'U'
					else:
						cart[2] = 'L'
					cart[3] = 0
		
			carts[i] = cart
			# Check collisions:
			for j in range(len(carts)):
				if i != j and not carts[j][4] in carts_down and cart[0] == carts[j][0] and cart[1] == carts[j][1]:
					collisions.append(cart[0:2])
					if(collision == 0):
						collision = 1
						first_collision = cart[0:2]
					carts_down.append(carts[i][4])
					carts_down.append(carts[j][4])
					break

print "First cart collision position: %d,%d"%(first_collision[1], first_collision[0])
for x in carts:
	if not x[4] in carts_down:
		print "Last cart standing: id=%d, pos=%d,%d"%(x[4], x[1], x[0])
		break
