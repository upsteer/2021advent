import sys

file = ""
if str(sys.argv[len(sys.argv)-1]) == 'test':
	file = "tests/"
data_file = file + "day5.txt"
hash_dict = {}
with open(data_file, 'r') as f:
	for line in f:
		a,b = line.strip().replace(" ", "").split("->")
		start_x, start_y = a.split(',')
		end_x, end_y = b.split(',')
		diff_x = abs(int(end_x) - int(start_x))
		diff_y = abs(int(end_y) - int(start_y))
		diff = diff_x or diff_y
		diff_dir = "x"
		if diff_x and diff_y:
			# print(f"{start_x}, {start_y}")
			# print("to")
			# print(f"{end_x}, {end_y}\n")
			for i in range(diff+1):
				end_x_temp = int(start_x)
				end_y_temp = int(start_y)
				if end_x_temp - int(end_x) == end_y_temp - int(end_y):
					if int(end_x) > int(start_x):
						end_x_temp += i
						end_y_temp += i
					else:
						end_x_temp -= i
						end_y_temp -= i
				elif int(end_x) > int(start_x):
					end_x_temp += i
					end_y_temp -= i
				else:
					end_x_temp -= i
					end_y_temp += i
				# print("---")
				# print(end_x_temp, end_y_temp)
				# print("---")
				if hash_dict.get(f"{end_x_temp},{end_y_temp}"):
					hash_dict[f"{end_x_temp},{end_y_temp}"] += 1
				else:
					hash_dict[f"{end_x_temp},{end_y_temp}"] = 1
			continue
		if not diff_x:
			diff_dir = "y"
		for i in range(diff+1):
			index = i
			if diff_dir == "x":
				if int(end_x) > int(start_x):
					index+=int(start_x)
				else:
					index+=int(end_x)
				if hash_dict.get(f"{index},{end_y}"):
					hash_dict[f"{index},{end_y}"] += 1
				else:
					hash_dict[f"{index},{end_y}"] = 1
			else:
				if int(end_y) > int(start_y):
					index+=int(start_y)
				else:
					index+=int(end_y)
				if hash_dict.get(f"{end_x},{index}"):
					hash_dict[f"{end_x},{index}"] += 1
				else:
					hash_dict[f"{end_x},{index}"] = 1
count = 0
for val in hash_dict:
	if hash_dict[val] >= 2:
		count+=1
print(count)


# For Part 1 comment out line 21 to 43



