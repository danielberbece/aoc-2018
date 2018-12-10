lines = [line.rstrip('\n') for line in open('in.txt')]
inputs =[int(x) for x in lines[0].split(' ')]

def get_sum((index, total)):
	child_nodes = inputs[index]
	index += 1
	metadatas = inputs[index]
	index += 1
	current_sum = 0
	tmp_sum = 0
	for i in range(child_nodes):
		(index, tmp_sum) = get_sum((index, total))
		current_sum += tmp_sum
	for i in range(index, index + metadatas):
		current_sum += inputs[i]

	return (index + metadatas, current_sum)

(last, total_sum) = get_sum((0,0))
print total_sum
