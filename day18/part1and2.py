# Python 3
def readInput(file):
	acres = [[-1] * 52]
	for line in file:
		ls = line.rstrip("\n")
		al = [-1]
		for c in ls:
			if c == '.':
				al.append(0)
			elif c == '|':
				al.append(1)
			else:
				al.append(2)
		al.append(-1)
		acres.append(al)
	acres.append([-1] * 52)
	return acres

def lookAround(i, j, area):
	trees = 0
	lumbers = 0
	for x in [-1, 0, 1]:
		for y in [-1, 0, 1]:
			if area[i + x][j + y] == 1:
				trees += 1
			elif area[i + x][j + y] == 2:
				lumbers += 1
	if area[i][j] == 1:
		trees -= 1
	elif area[i][j] == 2:
		lumbers -= 1

	return trees, lumbers

def myPrint(area):
	for i in range(1, len(area) - 1):
		for j in range(1, len(area[i]) - 1):
			if area[i][j] == 0:
				print(".", end="")
			elif area[i][j] == 1:
				print("|", end="")
			elif area[i][j] == 2:
				print("#", end="")
		print("")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def getPeriodicArea(area):
	dex = []
	dex.append(area)
	nextArea = [line[:] for line in area]
	z = 0
	one  = 0
	while True:
		nextArea = [line[:] for line in area]
		for i in range(1, len(area) - 1):
			for j in range(1, len(area[i]) - 1):
				trees, lumbers = lookAround(i, j, area)
				
				if area[i][j] == 0 and trees > 2:
					nextArea[i][j] = 1
				elif area[i][j] == 1 and lumbers > 2:
					nextArea[i][j] = 2
				elif area[i][j] == 2 and (lumbers < 1 or trees < 1):
					nextArea[i][j] = 0
		if not nextArea in dex:
			dex.append(nextArea)
		else:
			return z + 1, dex.index(nextArea), nextArea
		z += 1
		area = [line[:] for line in nextArea]


def future(minutes, area):
	nextArea = [line[:] for line in area]
	for _ in range(minutes):
		nextArea = [line[:] for line in area]
		for i in range(1, len(area) - 1):
			for j in range(1, len(area[i]) - 1):
				trees, lumbers = lookAround(i, j, area)
				
				if area[i][j] == 0 and trees > 2:
					nextArea[i][j] = 1
				elif area[i][j] == 1 and lumbers > 2:
					nextArea[i][j] = 2
				elif area[i][j] == 2 and (lumbers < 1 or trees < 1):
					nextArea[i][j] = 0
		area = [line[:] for line in nextArea]
	return nextArea

def getResourcesValue(area):
	trees = 0
	lumbers = 0
	for i in range(1, len(area) - 1):
		for j in range(1, len(area[i]) - 1):
			if area[i][j] == 1:
				trees += 1
			elif area[i][j] == 2:
				lumbers += 1
	return trees, lumbers

def main():
	file = open("in.txt")
	area = readInput(file)
	
	# Part 1
	futureArea = future(10, area)
	trees, lumbers = getResourcesValue(futureArea)
	print("Answer for part 1 is %d"%(trees * lumbers))
	
	# Part 2
	stepCurrent, stepBefore, periodicArea = getPeriodicArea(area)
	lastMinutes = (int(1000000000) - stepCurrent) % (stepCurrent - stepBefore)
	futureArea = future(lastMinutes, periodicArea)
	trees, lumbers = getResourcesValue(futureArea)
	print("Answer for part 2 is %d"%(trees * lumbers))
	
if __name__ == "__main__":
	main()

