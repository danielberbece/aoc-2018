s = []
line = ''
with open('in.txt') as fp:  
   line = fp.readline()

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

print len(s)