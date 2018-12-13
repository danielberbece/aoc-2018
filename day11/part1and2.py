def get_answer(st, end, serialNumber=7139):
	matrix = [[(((x + 10) * y + serialNumber) * (x + 10) / 100) % 10 - 5 for x in range(1,301)] for y in range(1,301)]
	partialSums = [[0 for x in range(300)] for y in range(300)]

	for i in range(1,300):
		partialSums[0][i] = partialSums[0][i - 1] + matrix[0][i]

	for i in range(1,300):
		partialSums[i][0] = partialSums[i - 1][0] + matrix[i][0]

	for i in range(1,300):
		for j in range(1,300):
			partialSums[i][j] += matrix[i][j] + partialSums[i-1][j] + partialSums[i][j-1] - partialSums[i-1][j-1]


	max_fuel = -9999
	patch_width = 1
	patch_location = [0,0]
	for k in range(st, end):
		for y in range(300 - k):
			for x in range(300 - k):
				patch_fuel = 0
				patch_fuel = partialSums[y + k][x + k] - partialSums[y][x + k] - partialSums[y + k][x] + partialSums[y][x]
				if patch_fuel > max_fuel:
					max_fuel = patch_fuel
					patch_width = k
					patch_location[0] = x + 2
					patch_location[1] = y + 2
					
	return patch_location, patch_width

print "Part 1: ", get_answer(3,4)
print "Part 2: ", get_answer(1,300)
