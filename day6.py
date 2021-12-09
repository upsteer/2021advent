import sys

file = ""
if str(sys.argv[len(sys.argv)-1]) == 'test':
	file = "tests/"
data_file = file + "day6.txt"

with open(data_file, 'r') as f:
    input = f.read()
    input = [int(inp) for inp in input.split(',')]

day_list = []
each_day = input
population = len(input)
for day in range(80):
	new_day = []
	add_new = 0
	for inp in each_day:
		if inp == 0:
			add_new += 1
			new_day.append(6)
		num = inp-1
		if num >= 0:
			new_day.append(num)
	for i in range(add_new):
		new_day.append(8)
	each_day = new_day
	print(len(each_day))

population = len(input)

print(population)
total_days = 80
for fish in each_day:
	temp_day = total_days - fish
	factor_8 = math.floor(temp_day/8)
	population += math.floor(math.pow(2, factor_8))

print(population*2)
