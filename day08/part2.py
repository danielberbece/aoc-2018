lines = [line.rstrip('\n') for line in open('in.txt')]
inputs =[int(x) for x in lines[0].split(' ')]

def get_sum(index):
	child_nodes = inputs[index]
	index += 1
	metadatas = inputs[index]
	index += 1
	current_sum = 0
	if child_nodes == 0:
		for i in range(metadatas):
			current_sum += inputs[index]
			index += 1
		return (index, current_sum)

	tmp = 0
	tmp_index = 0
	child_values = [0 for i in range(child_nodes)]
	for i in range(child_nodes):
		(tmp_index, tmp) = get_sum(index)
		child_values[i] = tmp
		index = tmp_index

	for i in range(index, index + metadatas):
		if inputs[i] <= child_nodes:
			current_sum += child_values[inputs[i] - 1]

	return (index + metadatas, current_sum)

(last, total_sum) = get_sum(0)
print total_sum
