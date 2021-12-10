import sys

file = ""
if str(sys.argv[len(sys.argv)-1]) == 'test':
	file = "tests/"
data_file = file + "day10.txt"

with open(data_file, 'r') as f:
    input = [line.strip() for line in f]

openers = ["(", "{", "[", "<"]
closers = [")", "}", "]", ">"]
stac = []
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
				break


print(total_points)
# print(count_o)
# print('close',count_c)

