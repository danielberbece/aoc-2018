import re

def getStars(file):
	stars = {}
	for line in file:
		stars[tuple(map(lambda x:int(x), re.findall(r"-?[0-9]+", line)))] = 1
	return stars

def dfs(currStar, stars, visitedStars):
	visitedStars[currStar] = 1
	for i in range(-3,4):
		for j in range(-3,4):
			for k in range(-3,4):
				for l in range(-3,4):
					if abs(i) + abs(j) + abs(k) + abs(l) <= 3:
						nextStar = (currStar[0] + i, currStar[1] + j, currStar[2] + k, currStar[3] + l)
						if nextStar in stars and not nextStar in visitedStars:
							dfs(nextStar, stars, visitedStars)

def main():
	file = open("in.txt")
	stars = getStars(file)
	visited = {}
	constelations = 0
	for star in stars:
		if not star in visited:
			constelations += 1
			dfs(star, stars, visited)
	print("Total constelations: %d"%constelations)

if __name__ == "__main__":
	main()