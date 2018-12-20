# Python 3
def getAnswers(regex):
	distances = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
	d = {(0, 0): 0}
	st = [(0, 0)]
	prev_x, prev_y = 0, 0
	x, y = 0, 0
	for i in regex:
		if i == '(':
			st.append((x, y))
		elif i == ')':
			x, y = st.pop()
		elif i == '|':
			x, y = st[-1]
		else:
			dx, dy = distances[i]
			x = prev_x + dx
			y = prev_y + dy
			if not (x, y) in d:
				d[(x, y)] = d[(prev_x, prev_y)] + 1
			elif d[(x, y)] > d[(prev_x, prev_y)] + 1:
				d[(x, y)] = d[(prev_x, prev_y)] + 1
		prev_x = x
		prev_y = y

	print("Answer for part 1 is %d"%max(d.values()))
	S = 0
	for j in d.values():
		if j >= 1000:
			S += 1
	print("Answer for part 2 is %d"%S)

def main():
	file = open("in.txt")
	regex = [line.rstrip("\n") for line in file][0][1:-1]
	getAnswers(regex)

if __name__ == "__main__":
	main()