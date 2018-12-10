pos_coords = []
max_x = 0
max_y = 0
lines = [line.rstrip('\n') for line in open('in.txt')]

for line in lines:
	coordstring = ''.join(line.split())
	coordx = int(coordstring.split(',')[0])
	coordy = int(coordstring.split(',')[1])
	pos_coords.append((coordx, coordy))
	if coordx > max_x:
		max_x = coordx
	if coordy > max_y:
		max_y = coordy

#make table:
table = [[(0,-1) for x in range(max_x + 2)] for y in range(max_y + 2)]
for x in range(len(pos_coords)):
	table[pos_coords[x][1]][pos_coords[x][0]] = (x + 1, 0)

		# coord        ,  id
queue = [(pos_coords[x], x + 1, 0) for x in range(len(pos_coords))]


while len(queue) != 0:
	tuple1 = queue[0]
	queue.pop(0)
	#move in directions:
	coord_x = tuple1[0][0]
	coord_y = tuple1[0][1]
	a_id = tuple1[1]
	dist = tuple1[2]

	#move left:
	if coord_x - 1 >= 0:
		if table[coord_y][coord_x - 1][1] == -1:
			table[coord_y][coord_x - 1] = (a_id, dist + 1)
			queue.append(((coord_x - 1, coord_y), a_id, dist + 1))
		elif table[coord_y][coord_x - 1][1] == dist + 1 and table[coord_y][coord_x - 1][0] != a_id:
			table[coord_y][coord_x - 1] = (0, -3)
			queue.append(((coord_x - 1, coord_y), a_id, dist + 1))

	#move right:
	if coord_x + 1 < max_x + 2:
		if table[coord_y][coord_x + 1][1] == -1:
			table[coord_y][coord_x + 1] = (a_id, dist + 1)
			queue.append(((coord_x + 1, coord_y), a_id, dist + 1))
		elif table[coord_y][coord_x + 1][1] == dist + 1 and table[coord_y][coord_x + 1][0] != a_id:
			table[coord_y][coord_x + 1] = (0, -3)
			queue.append(((coord_x + 1, coord_y), a_id, dist + 1))

	#move up:
	if coord_y - 1 >= 0:
		if table[coord_y - 1][coord_x][1] == -1:
			table[coord_y - 1][coord_x] = (a_id, dist + 1)
			queue.append(((coord_x, coord_y - 1), a_id, dist + 1))
		elif table[coord_y - 1][coord_x][1] == dist + 1 and table[coord_y - 1][coord_x][0] != a_id:
			table[coord_y - 1][coord_x] = (0, -3)
			queue.append(((coord_x, coord_y - 1), a_id, dist + 1))

	#move down:
	if coord_y + 1 < max_y + 2:
		if table[coord_y + 1][coord_x][1] == -1:
			table[coord_y + 1][coord_x] = (a_id, dist + 1)
			queue.append(((coord_x, coord_y + 1), a_id, dist + 1))
		elif table[coord_y + 1][coord_x][1] == dist + 1 and table[coord_y + 1][coord_x][0] != a_id:
			table[coord_y + 1][coord_x] = (0, -3)
			queue.append(((coord_x, coord_y + 1), a_id, dist + 1))

area_per_id = [0 for x in range(len(pos_coords) + 1)]
for line in table:
	for col in line:,
		area_per_id[col[0]] += 1


to_ignore = [0 for x in range(len(pos_coords) + 1)]
for x in range(max_x + 2):
	to_ignore[table[0][x][0]] = 1
	to_ignore[table[max_y + 1][x][0]] = 1
for y in range(max_y + 2):
	to_ignore[table[y][0][0]] = 1
	to_ignore[table[y][max_x + 1][0]] = 1

max_area = 0
for i in range(len(area_per_id)):
	if to_ignore[i] == 0 and i != 0 and max_area < area_per_id[i]:
		max_area = area_per_id[i]

print max_area





