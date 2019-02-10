from parse import *

def addr(instr, regs):
	regs[instr[3]] = regs[instr[1]] + regs[instr[2]]
def addi(instr, regs):
	regs[instr[3]] = regs[instr[1]] + instr[2]
def mulr(instr, regs):
	regs[instr[3]] = regs[instr[1]] * regs[instr[2]]
def muli(instr, regs):
	regs[instr[3]] = regs[instr[1]] * instr[2]
def banr(instr, regs):
	regs[instr[3]] = regs[instr[1]] & regs[instr[2]]
def bani(instr, regs):
	regs[instr[3]] = regs[instr[1]] & instr[2]
def borr(instr, regs):
	regs[instr[3]] = regs[instr[1]] | regs[instr[2]]
def bori(instr, regs):
	regs[instr[3]] = regs[instr[1]] | instr[2]
def setr(instr, regs):
	regs[instr[3]] = regs[instr[1]]
def seti(instr, regs):
	regs[instr[3]] = instr[1]
def gtir(instr, regs):
	if instr[1] > regs[instr[2]]:
		regs[instr[3]] = 1
	else:
		regs[instr[3]] = 0
def gtri(instr, regs):
	if regs[instr[1]] > instr[2]:
		regs[instr[3]] = 1
	else:
		regs[instr[3]] = 0
def gtrr(instr, regs):
	if regs[instr[1]] > regs[instr[2]]:
		regs[instr[3]] = 1
	else:
		regs[instr[3]] = 0
def eqir(instr, regs):
	if instr[1] == regs[instr[2]]:
		regs[instr[3]] = 1
	else:
		regs[instr[3]] = 0
def eqri(instr, regs):
	if regs[instr[1]] == instr[2]:
		regs[instr[3]] = 1
	else:
		regs[instr[3]] = 0
def eqrr(instr, regs):
	if regs[instr[1]] == regs[instr[2]]:
		regs[instr[3]] = 1
	else:
		regs[instr[3]] = 0

def find_opcodes(file):
	i = 0
	lines = [line.rstrip('\n') for line in file]
	fns = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtri,gtrr,gtir,eqrr,eqri,eqir]
	opcodes = [fns[:] for x in range(0,16)]
	total = 0
	while i < len(lines):
		if lines[i][0:6] == 'Before':
			p = parse("[{},{},{},{}]", lines[i][8:])
			# print(p)
			before_regs = [int(x) for x in p.fixed]
			i += 1
			
			instr = parse("{} {} {} {}", lines[i])
			instr = [int(x) for x in instr.fixed]
			i += 1
			p = parse("[{},{},{},{}]", lines[i][8:])
			after_regs = [int(x) for x in p.fixed]
			i += 1

			possible_ops = 0
			for f in fns:
				working_regs = [x for x in before_regs]
				f(instr, working_regs)
				if working_regs[instr[3]] == after_regs[instr[3]]:
					possible_ops += 1
				elif f in opcodes[instr[0]]:
					opcodes[instr[0]].remove(f)
			if possible_ops > 2:
				total += 1
		i += 1
	print("Answer for part 1 is %d"%total)
	
	found = []
	opcodes_f = [0 for x in range(16)]
	while len(found) != 16:
		for x in range(16):
			if len(opcodes[x]) == 1 and not opcodes[x][0] in found:
				found.append(opcodes[x][0])
				opcodes_f[x] = opcodes[x][0]
			else:
				for i in opcodes[x]:
					if i in found:
						opcodes[x].remove(i)

	return opcodes_f

def run(file, opcodes):
	regs = [0,0,0,0]
	for line in file:
		instr = parse("{} {} {} {}", line)
		instr = [int(x) for x in instr.fixed]
		opcodes[instr[0]](instr, regs)
	return regs


#main
file = open("in1.txt")
opcodes = find_opcodes(file)
file = open("in2.txt")
final_regs = run(file, opcodes)
print("Answer for part 2 is %d"%final_regs[0])
