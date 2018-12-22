# Python 3
import networkx as nx
def makeArea(depth, corner, target):
	tx = corner[0]
	ty = corner[1]
	depthModulo = depth % 20183
	area = [[0 for j in range(tx + 1)] for i in range(ty + 1)]
	for i in range(0, ty + 1):
		for j in range(0, tx + 1):
			if (j, i) == (0,0) or (j, i) == (target[0], target[1]):
				area[i][j] = depthModulo
			elif j == 0:
				area[i][j] = ((i * 48271) % 20183 + depthModulo) % 20183
			elif i == 0:
				area[i][j] = ((j * 16807) % 20183 + depthModulo) % 20183
			else:
				area[i][j] = ((area[i][j - 1] * area[i - 1][j]) % 20183 + depthModulo) % 20183

	for i in range(ty + 1):
		for j in range(tx + 1):
			area[i][j] = area[i][j] % 3

	return area

# rocky:  0: climbing gear or torch
# wet:    1: climbing gear or neither
# narrow: 2: torch or neither

# 0 climbing gear 
# 1 torch 
# 2 neither

def addEdge(G, p, pt, area):
	(x, y) = p
	(tx, ty) = pt
	if area[y][x] == 0:
		if area[ty][tx] == 0:
			G.add_edge((x, y, 0), (tx, ty, 0), weight=1)
			G.add_edge((x, y, 1), (tx, ty, 1), weight=1)
		elif area[ty][tx] == 1:
			G.add_edge((x, y, 0), (tx, ty, 0), weight=1)
		elif area[ty][tx] == 2:
			G.add_edge((x, y, 1), (tx, ty, 1), weight=1)
	elif area[y][x] == 1:
		if area[ty][tx] == 0:
			G.add_edge((x, y, 0), (tx, ty, 0), weight=1)
		elif area[ty][tx] == 1:
			G.add_edge((x, y, 0), (tx, ty, 0), weight=1)
			G.add_edge((x, y, 2), (tx, ty, 2), weight=1)
		elif area[ty][tx] == 2:
			G.add_edge((x, y, 2), (tx, ty, 2), weight=1)
	elif area[y][x] == 2:
		if area[ty][tx] == 0:
			G.add_edge((x, y, 1), (tx, ty, 1), weight=1)
		elif area[ty][tx] == 1:
			G.add_edge((x, y, 2), (tx, ty, 2), weight=1)
		elif area[ty][tx] == 2:
			G.add_edge((x, y, 1), (tx, ty, 1), weight=1)
			G.add_edge((x, y, 2), (tx, ty, 2), weight=1)


def addInternalEdge(G, x, y, area):
	if area[y][x] == 0:
		G.add_edge((x, y, 0), (x, y, 1), weight=7)
	elif area[y][x] == 1:
		G.add_edge((x, y, 0), (x, y, 2), weight=7)
	else:
		G.add_edge((x, y, 2), (x, y, 1), weight=7)

def dijkstra(area, target):
	G = nx.Graph()
	for i in range(target[1] + 101):
		for j in range(target[0] + 101):
			addInternalEdge(G, j, i, area)
			if i + 1 < target[1] + 101:
				addEdge(G, (j, i), (j, i + 1), area)
			if j + 1 < target[0] + 101:
				addEdge(G, (j, i), (j + 1, i), area)
			if i - 1 >= 0:
				addEdge(G, (j, i), (j, i - 1), area)
			if j - 1 >= 0:
				addEdge(G, (j, i), (j - 1, i), area)
	
	return nx.dijkstra_path_length(G, (0,0,1), (target[0], target[1], 1))


def readInput(file):
	
	inp = [line.rstrip("\n") for line in file]
	inp = [line.split(" ") for line in inp]
	inp = [inp[0][1], inp[1][1].split(',')[0], inp[1][1].split(',')[1]]
	inp = list(map(lambda x: int(x), inp))
	return inp[0], inp[1:]

def printArea(area):
	for y in area:
		for x in y:
			if x == 0:
				print(".", end="")
			elif x==1:
				print("=", end="")
			else:
				print("|", end="")
		print("")

def main():
	file = open("in.txt")
	depth, target = readInput(file)
	area = makeArea(depth, target, target)

	risk = 0
	for i in range(target[1] + 1):
		for j in range(target[0] + 1):
			risk += area[i][j]
	print("Part 1: %d"%risk)

	area = makeArea(depth, [target[0] + 100, target[1] + 100], target)
	minDist = dijkstra(area, target)
	print("Part 2: %d"%minDist)

if __name__ == "__main__":
	main()
