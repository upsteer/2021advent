import sys
import json

file = ""
if str(sys.argv[len(sys.argv)-1]) == 'test':
	file = "tests/"
data_file = file + "day11.txt"

with open(data_file, 'r') as f:
    input_data = [line.strip() for line in f]


zeros = """0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000"""
zero_input = [line.strip() for line in zeros.split('\n')]
hash_map = {}
flash = 0

def updateneighbour(coords):
	cases = [[-1,0], [-1,-1], [0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1]]
	coord = [int(x) for x in coords.split(",")]
	global flash
	another_flash = []
	for case in cases:
		place_x = coord[0] + case[0]
		place_y = coord[1] + case[1]
		where = f"{str(place_x)},{str(place_y)}"
		val = hash_map.get(where)
		if val:
			hash_map[where]+=1
			if hash_map[where] > 9:
				flash+=1
				another_flash.append(where)
				hash_map[where] = 0
	return another_flash

def add_one():
	untouchables = []
	global flash
	for octo in sorted(hash_map.keys()):
		octopus = hash_map[octo]
		if octopus == 9:
			flash+=1
			hash_map[octo] = 0
			untouchables.append(octo)
		else:
			hash_map[octo]+=1
	return untouchables

def print_pretty():
	print_str = ""
	line_limit = len(input_data[0])
	counter = 0
	for key in sorted(hash_map):
		print_str += f"{hash_map[key]}"
		counter += 1
		if counter >= line_limit:
			counter = 0
			print_str += "\n"
	print(print_str)

def initialize(input_data):
	hash_map = {}
	for j, line in enumerate(input_data):
		temp = []
		for i, depth in enumerate(line):
			hash_map[f"{str(j)},{str(i)}"] = int(line[i])
	return hash_map

hash_map = initialize(input_data)
zeros_map = initialize(zero_input)
zeros_hash = hash(json.dumps(zeros_map))
def call_again(get_nines):
	for nine in get_nines:
		subsiquent = updateneighbour(nine)
		if len(subsiquent) >= 1:
			call_again(subsiquent)

iters = 0
while True:
	iters+=1
	get_nines = add_one()
	call_again(get_nines)
	if iters == 100:
		print("Part 1", flash)
	if zeros_hash == hash(json.dumps(hash_map)):
		print("Part 2", iters)
		break

