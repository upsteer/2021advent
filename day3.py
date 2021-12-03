import sys
import copy

file = ""
if str(sys.argv[-1]) == 'test':
	file = "tests/"
data_file = file + "day3.txt"

with open(data_file, 'r') as f:
    input = [line.strip() for line in f]
total_bits = len(input[0])

def binarycounter(datum):
	final_count = []
	for i in range(total_bits):
		final_count.append({"one": 0, "zero": 0})
	for j, inp in enumerate(datum):
		for i in range(total_bits):
			if inp[i] == "1":
				final_count[i]["one"] += 1
			else:
				final_count[i]["zero"] += 1
	return final_count
part1 = binarycounter(input)
digit = ""
inv = ""
for data in part1:
	if data["one"] > data["zero"]:
		digit+="1"
		inv+="0"
	else:
		digit+="0"
		inv+="1"

print("part1", int(digit, 2)*int(inv, 2))
def air(invert=False):
	filtered = copy.deepcopy(input)
	final_count = copy.deepcopy(part1)
	i = 0
	checker = "0"
	invertor = "1"
	if invert:
		checker = "1"
		invertor = "0"
	while len(filtered) != 1:
		to_check = checker
		if final_count[i]["one"] >= final_count[i]["zero"]:
			to_check = invertor

		filtered = list(filter(lambda x: x[i] == to_check, filtered))
		final_count = binarycounter(filtered)
		i+=1
	return filtered[0]

print("part2", int(air(), 2)*int(air(invert=True), 2))






