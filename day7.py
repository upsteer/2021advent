import sys
import statistics
import math
file = ""
if str(sys.argv[len(sys.argv)-1]) == 'test':
	file = "tests/"
data_file = file + "day7.txt"

with open(data_file, 'r') as f:
    input = f.read()
    input = [int(inp) for inp in input.split(',')]

average = sum(input)/len(input)

sum_list = []
for inp in input:
	sum = 0
	for i in range(len(input)):
		diff = abs(inp-input[i])
		sum += diff
	sum_list.append(sum)
# print(sum_list)
print('part 1: ', min(sum_list))

fuel_arr = []

for num in range(int(max(input)/2)):
	fuel = 0
	# print(f"\n {num}")
	for inp in input:
		diff = abs(inp-num)
		curr_fuel = (diff)*(diff+1)/2
		# print(curr_fuel)
		fuel += curr_fuel
	fuel_arr.append(fuel)

# print('fuel_arr', fuel_arr)
print('fuel', min(fuel_arr))