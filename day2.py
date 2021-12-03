import sys

file = ""
if str(sys.argv[-1]) == 'test':
	file = "tests/"
data_file = file + "day2.txt"

with open(data_file, 'r') as f:
    input = [line.strip().split(' ') for line in f]

def move(input, first=False):
    position = {'horizontal': 0, 'depth': 0, 'aim': 0}
    for inp in input:
        if inp[0] == 'forward':
            position['horizontal'] += int(inp[1])
            if position['aim'] != 0 and not first:
                position['depth'] += int(inp[1])*position['aim']
        elif inp[0] == 'up':
            if first:
                position['depth'] -= int(inp[1])
            position['aim'] -= int(inp[1])
        elif inp[0] == 'down':
            if first:
                position['depth'] += int(inp[1])
            position['aim'] += int(inp[1])
    return position['horizontal']*position['depth']



print("first", move(input, first=True))
print("second", move(input))