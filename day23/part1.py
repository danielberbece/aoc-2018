from parse import *


def applySignal(nanobots, area):
	rx, ry, rz = 0, 0, 0

	visited = {(rx, ry, rz): 1}
	Q = [(rx, ry, rz)]
	while len(Q) != 0:
		p = Q[0]
		Q.pop(0)
		if abs(p[0]) + abs(p[1]) + abs(p[2]) <= 50:
			for nanobot in nanobots:
				if abs(p[0] - nanobot[0]) + abs(p[1] - nanobot[1]) + abs(p[2] - nanobot[2]) <= nanobot[3]:
					if (p[0], p[1], p[2]) in area:
						area[(p[0], p[1], p[2])] += 1
					else:
						area[(p[0], p[1], p[2])] = 1
					for (dx, dy, dz) in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
						newx, newy, newz = p[0] + dx, p[1] + dy, p[2] + dz
						if not (newx, newy, newz) in visited:
							visited[(newx, newy, newz)] = 1
							Q.append((newx, newy, newz))




def getNanobotsInRangeOf(nanobots, strongestId):
	sx, sy, sz = nanobots[strongestId][0], nanobots[strongestId][1], nanobots[strongestId][2]
	nrange = nanobots[strongestId][3]
	nanobotsInRange = 0
	for nanobot in nanobots:
		if abs(nanobot[0] - sx) + abs(nanobot[1] - sy) + abs(nanobot[2] - sz) <= nrange:
			nanobotsInRange += 1

	return nanobotsInRange

def getStrongestId(nanobots):
	maxPower = 0
	Id = 0
	for i in range(len(nanobots)):
		if nanobots[i][3] > maxPower:
			maxPower = nanobots[i][3]
			Id = i

	return Id

def getInput(file):
	nanobots = []
	for line in file:
		p = parse("pos=<{},{},{}>, r={}", line.rstrip("\n"))
		nanobots.append((int(p.fixed[0]), int(p.fixed[1]), int(p.fixed[2]), int(p.fixed[3])))
	return nanobots

def main():
	file = open("in.txt")
	nanobots = getInput(file)
	strongestId = getStrongestId(nanobots)
	nanobotsInRange = getNanobotsInRangeOf(nanobots, strongestId)
	print("Part 1: %d"%nanobotsInRange)

	areaSignal = {}
	applySignal(nanobots, areaSignal)

	strongestPoint = (0, 0, 0)
	power = 0
	for p in areaSignal:
		if power == areaSignal[p]:
			if abs(p[0]) + abs(p[1]) + abs(p[2]) < abs(strongestPoint[0]) + abs(strongestPoint[1]) + abs(strongestPoint[2]):
				strongestPoint = p
		elif power < areaSignal[p]:
			power = areaSignal[p]
			strongestPoint = p
	print(strongestPoint, power)

if __name__ == "__main__":
	main()