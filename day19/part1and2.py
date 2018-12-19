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

def sumOfDivisors(n):
	sum_ = 0
	for i in range(1, n + 1):
		if n % i == 0:
			sum_ += i
	return sum_

def runProgramO1(program, A, ip_reg):
	regs = [A,0,0,0,0,0]
	
	max_iter = 0
	while regs[ip_reg] >= 0 and regs[ip_reg] < len(program) and max_iter < 1000000: 
		instr = program[regs[ip_reg]]
		instr[1] = int(instr[1])
		instr[2] = int(instr[2])
		instr[3] = int(instr[3])
		op_index = opcode_names.index(instr[0])
		opcodes[op_index](instr, regs)
		regs[ip_reg] += 1
		max_iter += 1

	if max_iter == 1000000:
		return sumOfDivisors(regs[3])
	else:
		return regs[0]
	
def realProgram(A):
	D = 2
	D *= D
	D *= 19
	D *= 11
	B = 5
	B *= 22
	B += 2
	D += B
	if (A == 1):
		B = 27
		B *= 28
		B += 29
		B *= 30
		B *= 14
		B *= 32
		D += B
	ok = 1
	
	return sumOfDivisors(D)

def main():
	file = open("in.txt")
	program = getProgram(file)
	ip_reg = int(program[0][1])
	program.pop(0)
	result = runProgramO1(program, 0, ip_reg)
	print("Answer for part 1 is: %d"%result)

	result = runProgramO1(program, 1, ip_reg)
	print("Answer for part 2 is: %d"%result)

if __name__ == "__main__":
	main()