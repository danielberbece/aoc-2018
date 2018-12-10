import string

def react(line):
	s = []
	for letter in line:
		if len(s) != 0:
			prevLetter = s[len(s) - 1]
			if prevLetter.isupper() and prevLetter.lower() == letter:
				s.pop()
			else: 
				if letter.isupper() and prevLetter == letter.lower():
					s.pop()
				else:
					s.append(letter)
		else:
			s.append(letter)

	return len(s)



line = ''
with open('in.txt') as fp:  
   line = fp.readline()

best_len = 20000
for letter in string.ascii_lowercase:
	newPolimer = line.replace(letter, '').replace(letter.upper(), '')
	tmp = react(newPolimer)
	if(tmp < best_len):
		best_len = tmp
		best_Poli = newPolimer

print best_len

