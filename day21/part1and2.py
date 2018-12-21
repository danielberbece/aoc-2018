# Python 3, but must run with pypy for part 2
# as it takes a lot of time
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

opcodes = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtri,gtrr,gtir,eqrr,eqri,eqir]
opcode_names = ["addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtri","gtrr","gtir","eqrr","eqri","eqir"]

def getProgram(file):
	p = [line.rstrip("\n").split(" ") for line in file]
	return p

def runProgramO1(program, ip_reg, part):
	regs = [0,0,0,0,0,0]
	
	max_iter = 0
	last_found = 0
	vals = {}
	last_value = 0
	while regs[ip_reg] >= 0 and regs[ip_reg] < len(program): # and max_iter < 100000000: 
		if regs[ip_reg] == 28:
			if not regs[5] in vals:
				vals[regs[5]] = max_iter
				last_value = regs[5]
				if part == 1:
					break
			else:
				break
		instr = program[regs[ip_reg]]
		op_index = opcode_names.index(instr[0])
		opcodes[op_index](instr, regs)
		regs[ip_reg] += 1
		max_iter += 1

	print("Solution for part %d is %d"%(part, last_value))

def optimiseCode(program):
	for i in range(len(program)):
		program[i][1] = int(program[i][1])
		program[i][2] = int(program[i][2])
		program[i][3] = int(program[i][3])

def main():
	file = open("in.txt")
	program = getProgram(file)
	ip_reg = int(program[0][1])
	program.pop(0)
	optimiseCode(program)
	runProgramO1(program, ip_reg, 1)
	runProgramO1(program, ip_reg, 2)
	
if __name__ == "__main__":
	main()