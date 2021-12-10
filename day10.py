import sys

file = ""
if str(sys.argv[len(sys.argv)-1]) == 'test':
	file = "tests/"
data_file = file + "day10.txt"

with open(data_file, 'r') as f:
    input = [line.strip() for line in f]

openers = ["(", "[", "{" ,"<"]
closers = [")", "]", "}", ">"]
stacks = []
valid = []
mapper = {
	"(": ")",
	"[": "]",
	"{": "}",
	"<": ">"
}
points={
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137
}

total_points = 0
for inp in input:
	stac = []
	error = False
	for sym in inp:
		if sym in openers:
			stac.append(sym)
		elif sym in closers:
			opener = stac[-1:]
			if mapper.get(opener[0]) == sym:
				stac.pop()
			else:
				total_points+=points.get(sym)
				error = True
				break
	if not error:
		stacks.append(stac)

print('Part 1', total_points)
skores = []
for st in stacks:
	sum = 0
	for open in reversed(st):
		sum*=5
		sum+=openers.index(open)+1
	skores.append(sum)

print('Part 2', sorted(skores)[int((len(skores)-1)/2)])
