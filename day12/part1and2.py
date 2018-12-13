import re
lines = []
with open("in.txt") as file:
	for line in file:
		lines.append(line.rstrip("\n"))
initial_pots = re.findall(r'[#.]+',lines[0])[0]
rules = []
for i in range(2, len(lines)):
	match = re.findall(r'[#.]+', lines[i])
	if match[1] == '#':
		rules.append(match[0])

pots = initial_pots
new_pots = pots
dex = []
first_dex = []

k = 0
first_pos = 0
pots_20 = []
firts_pos_20 = 0
while not pots in dex:
	if k == 20:
		pots_20 = pots
		firts_pos_20 = first_pos

	dex.append(pots)
	first_dex.append(first_pos)
	tmp_pots = '.....' + pots + '.....'
	first_pos -= 5
	new_pots = tmp_pots
	for i in range(len(tmp_pots) - 5):
		rule_matched = 0
		for rule in rules:
			if tmp_pots[i:i+5] == rule:
				new_pots = new_pots[0:i+2] + '#' + new_pots[i + 3:]
				rule_matched = 1

		if rule_matched != 1:
			new_pots = new_pots[0:i+2] + '.' + new_pots[i+3:]
	j = 0
	while new_pots[j] == '.':
		first_pos += 1
		new_pots = new_pots[j + 1:]

	new_pots = new_pots.rstrip('.')
	pots = new_pots
	k += 1

total = 0
for i in range(len(pots_20)):
	if pots_20[i] == '#':
		total += i + firts_pos_20
print "Pots value at epoch 20: %d"%total

head = int(5e10) - k + first_pos
total = 0
diez = 0
for i in range(len(pots)):
	if pots[i] == '#':
		diez += 1
		total += i + head
print "Pots value at epoch 50000000000: %d"%total