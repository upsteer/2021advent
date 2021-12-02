import sys

file = ""
if str(sys.argv[len(sys.argv)-1]) == 'test':
	file = "tests/"
data_file = file + "day1.txt"

def increment_counter(data):
	counter = 0;
	for index in range(1, len(data)):
		if(data[index] - data[index-1]>0):
			counter+=1
	return counter

with open(data_file, 'r') as f:
    input = [int(line.strip()) for line in f]
    print(f"first {increment_counter(input)}")

windows = []
for index in range(1, len(input)-1):
	window = input[index-1] + input[index] + input[index+1]
	windows.append(window)

print(f"second {increment_counter(windows)}")

