import sys

file = ""
if str(sys.argv[len(sys.argv)-1]) == 'test':
	file = "tests/"
data_file = file + "day9.txt"

with open(data_file, 'r') as f:
    input = [line.strip() for line in f]

heat_map = {}
heat_obj = {}
for j, line in enumerate(input):
	for i, depth in enumerate(line):
		heat_map[f"{str(i)},{str(j)}"] = line[i]
		# heat_obj[str(j)+str[i]] = line[i]
dirs = [(0,1), (1,0), (-1,0), (0,-1)]
print(heat_map)
result = []
resulting_lows = []
for heat in heat_map:
	x, y = heat.split(',')
	value = heat_map.get(heat)
	temp_value = []
	for dir in dirs:
		tempx = int(x) + dir[0]
		tempy = int(y) + dir[1]
		temp_val = heat_map.get(f"{tempx},{tempy}")
		if temp_val:
			temp_value.append(temp_val)
	if min(temp_value) > value:
		resulting_lows.append(heat)
		result.append(value)

sum = 0
for res in result:
	sum += (int(res) + 1)
print(sum)

#for Part 2, Solution from Part 1 will suffice
# Starting from the points in Part 1, expant outward
# till you get a 9. For each positions, save it and then calculate its
# length then multiply for answer.
seen = []
def check_up_down(lows):
	# print(lows)
	x, y = lows.split(',')
	if lows in seen:
		return
	seen.append(lows)
	for dir in dirs:
		tempx = int(x) + dir[0]
		tempy = int(y) + dir[1]
		temp_val = heat_map.get(f"{tempx},{tempy}")
		if temp_val and temp_val!=str(9) and f"{tempx},{tempy}" not in seen:
			check_up_down(f"{tempx},{tempy}")
	return len(seen)

# print(resulting_lows)
count_arr = []
answer = 1
for lows in resulting_lows:
	sinks = check_up_down(lows)
	count_arr.append(sinks)
	seen = []

for _ in range(3):
	answer*=max(count_arr)
	count_arr.remove(max(count_arr))
print(answer)



