lines = [line.rstrip('\n') for line in open('in.txt')]
# lines = [line.rstrip('\n') for line in open('test.in')]

lines.sort()

matrix = [[0 for x in range(62)] for y in range(8000)]

i = 0
guard_id = ''
while i < len(lines):
	if lines[i][25] == '#':
		guard_id = ''
		k = 26
		while lines[i][k] != ' ':
			guard_id += lines[i][k]
			k += 1
		# print '#',int(guard_id)

		i += 1
	
	if lines[i][19] == 'f':
		start_sleep = lines[i][15:17]
		i += 1
		fin_sleep = lines[i][15:17]
		
		for x in range(int(start_sleep), int(fin_sleep)):
			matrix[int(guard_id)][60] += 1
			matrix[int(guard_id)][x] += 1

		i += 1
		# print matrix[int(guard_id)][60]

best_id = 0
best_time = 0
for i in range(8000):
	if matrix[i][60] > best_time:
		best_time = matrix[i][60]
		best_id = i

top = 0
top_minute = 0
for i in range(60):
	if matrix[best_id][i] > top:
		top_minute = i
		top = matrix[best_id][i]

print "#" + str(best_id)
print "minute " + str(top_minute)
print top_minute * best_id