visited = [0 for x in range(26)]
exists = [0 for x in range(26)]
lines = [line.rstrip('\n') for line in open('in.txt')]
graph = [[] for x in range(26)]
revgraph = [[] for x in range(26)]
for line in lines:
	node1 = ord(line[5]) - ord('A')
	node2 = ord(line[36]) - ord('A')
	exists[node1] = 1
	exists[node2] = 1
	graph[node1].append(node2)
	revgraph[node2].append(node1)

#find root nodes:
queue = []
for x in range(26):
	if len(revgraph[x]) == 0 and exists[x] == 1:
		queue.append(x)

queue.sort()
sol = []
while(len(queue) != 0):
	node = queue[0]
	
	queue.pop(0)
	sol.append(chr(node + ord('A')))
	for neigh in graph[node]:
		visited[neigh] += 1
		if visited[neigh] == len(revgraph[neigh]):
			queue.append(neigh)
			queue.sort()

print ''.join(sol)





