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

area = 0
for x in range(max_x + 1):
	for y in range(max_y + 1):
		total_dist = 0
		for (a_x, a_y) in pos_coords:
			total_dist += abs(x - a_x) + abs(y - a_y)
		if total_dist < 10000:
			area += 1
print area
