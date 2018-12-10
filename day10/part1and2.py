from parse import *
in_lines = [line.rstrip('\n') for line in open('in.txt')]

params_text = [parse("position=<{},{}> velocity=<{},{}>", x) for x in in_lines]
points = [(int(x[0]), int(x[1])) for x in params_text]
velcities = [(int(x[2]), int(x[3])) for x in params_text]
step = 0
found = 0

while found == 0:
	max_x = -999999
	max_y = -999999
	min_x = 999999
	min_y = 999999
	for point in points:
		if point[0] > max_x:
			max_x = point[0]
		if point[0] < min_x:
			min_x = point[0]

		if point[1] > max_y:
			max_y = point[1]
		if point[1] < min_y:
			min_y = point[1]

	if max_y - min_y == 9:
		found = 1
		print("Seconds: %d"%step)
		print("")
		for i in range(min_y, max_y + 1):
			for j in range(min_x, max_x + 1):
				if (j, i) in points:
					print("#", end='')
				else:
					print(" ", end='')
			print(" ")
	
	step += 1
	#move stars
	for i in range(len(points)):
		points[i] = (points[i][0] + velcities[i][0], points[i][1] + velcities[i][1])
