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
def calculate_who_won(boards, mixed_boards, draw):
	def max_indexer(lines):
		index_list = []
		num_list = []
		win_index_list = []
		for inn, line in enumerate(lines):
			max_index = 0
			max_num = 0
			win_index = 0
			for num in line:
				if draw.index(num)>max_index:
					max_index = draw.index(num)
					max_num = num
					win_index = inn
			index_list.append(max_index)
			num_list.append(max_num)
			win_index_list.append(win_index)
		return (min(index_list),
			num_list[index_list.index(min(index_list))],
			win_index_list[index_list.index(min(index_list))])

	(min_i_h, draw_num_h, win_ind_h) = max_indexer(boards)
	(min_i_v, draw_num_v, win_ind_v) = max_indexer(mixed_boards)
	fast_draw = draw_num_h
	final_board = boards
	winner_board = win_ind_h
	if min_i_h > min_i_v:
		fast_draw = draw_num_v
		final_board = mixed_boards
		winner_board = win_ind_v
		print("won vertical")

	board_num = winner_board-winner_board%5
	winner = final_board[board_num:board_num+5]
	return winner, fast_draw, board_num 

board_won, fastest_draw, board_number = calculate_who_won(boards, mixed_boards, draw)
draw_copy = draw[0:draw.index(fastest_draw)+1]
sum=0
untouched = []
for line in board_won:
	for num in line:
		if not num in draw_copy:
			sum+=num
			untouched.append(num)
print('Part 1', sum, fastest_draw, sum*fastest_draw)

print('won', board_number)
while len(boards) > 5:
	del boards[board_number:board_number+5]
	del mixed_boards[board_number:board_number+5]
	print(boards)
	print(mixed_boards)
	board_won, fastest_draw, board_number = calculate_who_won(boards, mixed_boards, draw)
	draw_copied = draw[0:draw.index(fastest_draw)+1]
	sum=0
	untouched = []
	for line in board_won:
		for num in line:
			if not num in draw_copied:
				sum+=num
				untouched.append(num)
	print(sum, fastest_draw, sum*fastest_draw)








