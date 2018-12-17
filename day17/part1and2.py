# Python 3
import sys
from parse import *

def readInput(file):
	ans = {}
	for line in file:
		lines = line.rstrip("\n")
		if lines[0] == 'x':
			p = parse("x={}, y={}..{}", lines)
			for y in range(int(p.fixed[1]), int(p.fixed[2]) + 1):
				ans[(int(p.fixed[0]), y)] = 1
		else:
			p = parse("y={}, x={}..{}", lines)
			for x in range(int(p.fixed[1]), int(p.fixed[2]) + 1):
				ans[(x, int(p.fixed[0]))] = 1
	return ans

def getBoundingBox(clayPoints):
	minX = 1000000
	minY = 1000000
	maxX = 0
	maxY = 0
	for (x, y) in clayPoints:
		if maxX < x:
			maxX = x
		if minX > x:
			minX = x
		if maxY < y:
			maxY = y
		if minY > y:
			minY = y
	return minX,minY,maxX,maxY

def settleWater(point, waterPoints, settledWater, blockedPoints):
	leftB = 0
	rightB = 0
	p = point
	while (p[0]-1, p[1]) in waterPoints:
		p = (p[0]-1, p[1])
	leftPoint = p
	if (p[0]-1,p[1]) in blockedPoints:
		leftB = 1
	if leftB == 1:
		p = point
		while (p[0]+1, p[1]) in waterPoints:
			p = (p[0]+1, p[1])
		rightPoint = p
		if (p[0]+1,p[1]) in blockedPoints:
			rightB = 1
		if rightB == 1:
			while leftPoint[0] <= rightPoint[0]:
				blockedPoints[leftPoint] = 1
				settledWater[leftPoint] = 1
				leftPoint = (leftPoint[0]+1, leftPoint[1])


def generateWater(point, waterPoints, settledWater, blockedPoints, maxY):
	if(point[1] > maxY):
		pass
	else:
		waterPoints[point] = 1
		if not (point[0], point[1] + 1) in blockedPoints:
			generateWater((point[0], point[1] + 1), waterPoints, settledWater, blockedPoints, maxY)
			settleWater((point[0], point[1] + 1), waterPoints, settledWater, blockedPoints)
		if (point[0], point[1] + 1) in blockedPoints:
			if not (point[0]-1, point[1]) in blockedPoints and not (point[0]-1, point[1]) in waterPoints:
				generateWater((point[0]-1, point[1]), waterPoints, settledWater, blockedPoints, maxY)
			if not (point[0]+1, point[1]) in blockedPoints and not (point[0]+1, point[1]) in waterPoints:
				generateWater((point[0]+1, point[1]), waterPoints, settledWater, blockedPoints, maxY)

def getAnswer(clayPoints):
	sys.setrecursionlimit(3000)
	boundingBox = getBoundingBox(clayPoints)
	settledWater = {}
	waterPoints = {}
	root = (500, 0)
	generateWater(root, waterPoints, settledWater, clayPoints, boundingBox[3])
	t1 = 0
	for p in waterPoints:
		if p[1] <= boundingBox[3] and p[1] >= boundingBox[1]:
			t1 += 1 
	print("Answer for part 1 is %d"%t1)
	t2 = 0
	for p in settledWater:
		if p[1] <= boundingBox[3] and p[1] >= boundingBox[1]:
			t2 += 1 
	print("Answer for part 2 is %d"%t2)

def main():
	file = open("in.txt")
	clayPoints = readInput(file)
	getAnswer(clayPoints)

if __name__ == "__main__":
	main()
