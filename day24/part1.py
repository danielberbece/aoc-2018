from parse import *
import re







# group == [units, hit points, [weaknesses], [immunities], damage_points, damage_type, initiative, id] == group
# army == [group1, group2, ...] == army

def getWords(line):
	words = re.findall(r"[a-z]+", line)
	return words

def makeGroup1(params, Id):
	group = []
	group.append(int(params[0]))
	group.append(int(params[1]))
	p = parse("(weak to {}; immune to {})", params[2])
	if p == None:
		p = parse("(immune to {}; weak to {})", params[2])
		if p == None:
			p = parse("(weak to {})", params[2])
			if p == None:
				p = parse("(immune to {})", params[2])
				im = getWords(p.fixed[0])
				group.append([])
				group.append(im)
			else:
				weaknesses = getWords(p.fixed[0])
				group.append(weaknesses)
				group.append([])
		else:
			im = getWords(p.fixed[0])
			weaknesses = getWords(p.fixed[1])
			group.append(weaknesses)
			group.append(im)
	else:
		im = getWords(p.fixed[1])
		weaknesses = getWords(p.fixed[0])
		group.append(weaknesses)
		group.append(im)
	group.append(int(params[3]))
	group.append(params[4])
	group.append(int(params[5]))
	group.append(Id)

	return group

def makeGroup2(params, Id):
	group = []
	group.append(int(params[0]))
	group.append(int(params[1]))
	group.append([])
	group.append([])
	group.append(int(params[2]))
	group.append(params[3])
	group.append(int(params[4]))
	group.append(Id)
	return group

def getArmies(file):
	immuneSystem = []
	armiesIds = 1
	infection = []
	currentArmy = None
	for line in file:
		sline = line.rstrip("\n")
		if sline == "Immune System:":
			currentArmy = immuneSystem
			continue
		elif sline == "Infection:":
			currentArmy = infection
			armiesIds = 101
			continue
		elif sline == "":
			continue
		else:
			group = []
			p = parse("{} units each with {} hit points {} with an attack that does {} {} damage at initiative {}", sline)
			if p == None:
				p = parse("{} units each with {} hit points with an attack that does {} {} damage at initiative {}", sline)
				group = makeGroup2(p.fixed, armiesIds)
				currentArmy.append(group)
			else:
				group = makeGroup1(p.fixed, armiesIds)
				currentArmy.append(group)
			armiesIds += 1
	
	return immuneSystem, infection

def sortDescending(allGroups):
	s = sorted(allGroups, key=lambda group: group[6], reverse=True)
	return sorted(s, key=lambda group: group[0] * group[4], reverse=True)

def getDefendant(group, defArmy, attackedIds):
	possibleDefGroups = []
	for g in defArmy:
		if not group[5] in g[3] and not g[7] in attackedIds:
			possibleDefGroups.append(g[:])
	if possibleDefGroups == []:
		return -1
	s = sorted(possibleDefGroups, key=lambda group: group[6], reverse=True)
	s = sorted(s, key=lambda g:g[0]*g[4], reverse=True)
	s = sorted(s, key=lambda g:((group[0] * group[4] * 2) if group[5] in g[2] else (group[0] * group[4])), reverse=True)
	return s[0][7]

def getGroupWithId(army, Id):
	for i in range(len(army)):
		if army[i][7] == Id:
			return i

def fight(immuneSystem, infection, part1=True):
	initiatives = {}
	for group in immuneSystem:
		initiatives[group[7]] = group[6]
	for group in infection:
		initiatives[group[7]] = group[6]

	boost = 0	# Manual binary search for the win
	copyImmune = [el[:] for el in immuneSystem]
	copyInf = [el[:] for el in infection]

	while True:
		infection = [el[:] for el in copyInf]
		immuneSystem = [el[:] for el in copyImmune]

		for i in range(len(immuneSystem)):
			immuneSystem[i][4] += boost
		boost += 1

		while len(immuneSystem) != 0 and len(infection) != 0:
			allGroups = sortDescending(immuneSystem[:] + infection[:])
			attacks = []
			attackedIds = []
			for group in allGroups:
				if group[7] > 100:	# group is infection, looking for immuneSystem
					grId = getDefendant(group, immuneSystem, attackedIds)
					if grId != -1:
						attacks.append((group[7], grId))
						attackedIds.append(grId)
				else:
					grId = getDefendant(group, infection, attackedIds)
					if grId != -1:
						attacks.append((group[7], grId))
						attackedIds.append(grId)

			sAttacks = sorted(attacks, key=lambda attack: initiatives[attack[0]], reverse=True)
			nDamagedGroups = 0

			for att in sAttacks:
				attId, defId = att[0], att[1]
				if attId > 100:	# attack from Infection:
					infIndex = getGroupWithId(infection, attId)
					immIndex = getGroupWithId(immuneSystem, defId)
					if infIndex != None and immIndex != None:
						mul = 1
						if infection[infIndex][5] in immuneSystem[immIndex][2]:
							mul = 2
						deadUnits = (infection[infIndex][0] * infection[infIndex][4] * mul) // immuneSystem[immIndex][1]
						if deadUnits != 0:
							nDamagedGroups += 1
						immuneSystem[immIndex][0] -= deadUnits
						if immuneSystem[immIndex][0] <= 0:
							immuneSystem.pop(immIndex)
				else:	# attack from imm:
					infIndex = getGroupWithId(infection, defId)
					immIndex = getGroupWithId(immuneSystem, attId)
					if infIndex != None and immIndex != None:
						mul = 1
						if immuneSystem[immIndex][5] in infection[infIndex][2]:
							mul = 2
						deadUnits = (immuneSystem[immIndex][0] * immuneSystem[immIndex][4] * mul) // infection[infIndex][1]
						if deadUnits != 0:
							nDamagedGroups += 1
						infection[infIndex][0] -= deadUnits
						if infection[infIndex][0] <= 0:
							infection.pop(infIndex)
			if nDamagedGroups == 0:
				break
		if len(infection) == 0 or part1 == True:
			break

	if len(infection) == 0:
		print("Remaining immune system units: %d with boost %d"%(sum(v[0] for v in immuneSystem), boost -1 ))
	else:
		print("Remaining infection units: %d"%(sum(v[0] for v in infection)))


def main():
	file = open("in.txt")
	immuneSystem, infection = getArmies(file)
	fight(immuneSystem, infection)
	file = open("in.txt")
	immuneSystem, infection = getArmies(file)
	fight(immuneSystem, infection, False)
if __name__ == "__main__":
	main()