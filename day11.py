import sys

file = ""
if str(sys.argv[len(sys.argv)-1]) == 'test':
	file = "tests/"
data_file = file + "day11.txt"

with open(data_file, 'r') as f:
    input = [line.strip() for line in f]

class Map:
	def __init__(self,x,y,energy):
		self.x = x
		self.y = y
		self.energy = energy

	def give_

heat_map = {}
nates = []
for j, line in enumerate(input):
	for i, depth in enumerate(line):
		heat_map[f"{str(i)},{str(j)}"] = line[i]
		point = Map(i, j, line[i])
		nates.append(point)

