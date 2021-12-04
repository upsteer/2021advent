import sys

file = ""
if str(sys.argv[len(sys.argv)-1]) == 'test':
	file = "tests/"
data_file = file + "day4.txt"


with open(data_file, 'r') as f:
    input = [line.strip().rstrip().split('\n') for line in f]

draw = list(map(lambda x: int(x), input[0][0].split(',')))
input.append([""])
boards = []
board = []
for index in range(1, len(input)):
	if not input[index][0]:
		if board:
			boards.append(board)
		board = []
	aa = list(map(lambda x: int(x), input[index][0].split()))
	if aa:
		boards.append(aa)

mixed_dict = {}
for index in range(5):
	new_line = []
	for b_index, b in enumerate(boards):
		new_line.append(b[index])
		if len(new_line) == 5:
			mixed_dict[b_index+index] = new_line
			new_line = []
mixed_boards = []
for li in sorted(mixed_dict.keys()):
	mixed_boards.append(mixed_dict[li])

print("horizontal \n", boards)
print("vertical \n", mixed_boards)
print("draw \n", draw)
def max_indexer(lines):
	index_list = []
	num_list = []
	for line in lines:
		max_index = 0
		max_num = 0
		for num in line:
			if draw.index(num)>max_index:
				max_index = draw.index(num)
				max_num = num
		index_list.append(max_index)
		num_list.append(max_num)
	return (min(index_list),
		num_list[index_list.index(min(index_list))])

(min_i_h, draw_num_h) = max_indexer(boards)
(min_i_v, draw_num_v) = max_indexer(mixed_boards)
fast_draw = draw_num_v
final_board = mixed_boards
winner_board = min_i_v
if draw_num_h > draw_num_v:
	fast_draw = draw_num_h
	winner_board = min_i_h
	final_board = boards
	print("won horizontal")

winner = final_board[winner_board-winner_board%5:winner_board-winner_board%5+5]
print(winner)
draw = draw[0:draw.index(fast_draw)+1]
sum=0
for line in winner:
	for num in line:
		if not num in draw:
			sum+=num
print(sum, fast_draw, sum*fast_draw)











