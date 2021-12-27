import sys

file = ""
if str(sys.argv[len(sys.argv)-1]) == 'test':
	file = "tests/"
data_file = file + "day6.txt"

with open(data_file, 'r') as f:
    input = f.read()
    input = [int(inp) for inp in input.split(',')]


count_arr = [0,0,0,0,0,0,0,0,0]

for inp in input:
	if count_arr[inp]:
		count_arr[inp]+=1
	else:
		count_arr[inp]=1

for i in range(256):
	at_zero = count_arr.pop(0)
	if at_zero != 0:
		count_arr.append(at_zero)
		count_arr[6]+=at_zero
	else:
		count_arr.append(0)

print(sum(count_arr))

