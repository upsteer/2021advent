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
	# print(day)
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
	# print(",".join(str(v) for v in new_day))
	each_day = new_day
	print(len(each_day))
# print(len(each_day))
