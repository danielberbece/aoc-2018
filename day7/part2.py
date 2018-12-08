
durations = [60 + x + 1 for x in range(26)]
workers = [[-1, 0], [-1, 0], [-1, 0], [-1, 0], [-1, 0]]
steps_to_do = 0
def worker_free():
	for x in workers:
		if x[1] == 0:
			return True
	return False

def get_free_worker():
	for x in range(5):
		if workers[x][1] == 0:
			return x

def do_work():
	for i in range(5):
		if(workers[i][1] != 0):
			workers[i][1] -= 1

def check_workers_done():
	ret = []
	for i in range(5):
		if(workers[i][1] == 0):
			ret.append(workers[i][0])
			workers[i][0] = -1
	return ret

visited = [0 for x in range(26)]
exists = [0 for x in range(26)]
lines = [line.rstrip('\n') for line in open('in.txt')]
graph = [[] for x in range(26)]
revgraph = [[] for x in range(26)]
for line in lines:
	node1 = ord(line[5]) - ord('A')
	node2 = ord(line[36]) - ord('A')
	if(exists[node1] == 0):
		exists[node1] = 1
		steps_to_do += 1
	if(exists[node2] == 0):
		exists[node2] = 1
		steps_to_do += 1

	graph[node1].append(node2)
	revgraph[node2].append(node1)

#find root nodes:
queue = []
for x in range(26):
	if len(revgraph[x]) == 0 and exists[x] == 1:
		queue.append(x)

queue.sort()
sol = []
time = 0
while(steps_to_do != 0):
	while worker_free() and len(queue) != 0:
		node = queue[0]
		queue.pop(0)
		worker = get_free_worker()
		workers[worker][0] = node
		workers[worker][1] = durations[node]

	do_work()
	time += 1

	done = check_workers_done()
	for e in done:
		if e != -1:
			steps_to_do -= 1
			for neigh in graph[e]:
				visited[neigh] += 1
				if visited[neigh] == len(revgraph[neigh]):
					queue.append(neigh)
					queue.sort()


print time






