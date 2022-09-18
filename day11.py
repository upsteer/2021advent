import sys

file = ""
if str(sys.argv[len(sys.argv)-1]) == 'test':
	file = "tests/"
data_file = file + "day11.txt"

with open(data_file, 'r') as f:
    input_data = [line.strip() for line in f]

class Map:
	def __init__(self,x,y,energy):
		self.x = x
		self.y = y
		self.energy = energy


	def __repr__(self):
		return f"[{self.x}, {self.y}, {self.energy}]"
		# return f"{self.energy}"

hash_map = {}
def updateneighbour(coords):
	cases = [[-1,0], [-1,-1], [0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1]]
	coord = [int(x) for x in coords.split(",")]
	for case in cases:
		place_x = coord[0] + case[0]
		place_y = coord[1] + case[1]
		where = f"{str(place_x)},{str(place_y)}"
		if hash_map.get(where):
			hash_map[where]+=1

def add_one():
	untouchables = []
	for octo in sorted(hash_map.keys()):
		octopus = hash_map[octo]
		if octopus == 9:
			hash_map[octo] = 0
			untouchables.append(octo)
		else:
			hash_map[octo]+=1
	print("untouchables", untouchables)
	return untouchables

nates = []
for j, line in enumerate(input_data):
	temp = []
	for i, depth in enumerate(line):
		hash_map[f"{str(i)},{str(j)}"] = int(line[i])
		point = Map(i, j, line[i])
		temp.append(point)
	nates.append(temp)

print(hash_map)
get_nines = add_one()
for nine in get_nines:
	updateneighbour(nine)
print_pretty(hash_map)
