import sys

file = ""
if str(sys.argv[len(sys.argv)-1]) == 'test':
	file = "tests/"
data_file = file + "day8.txt"

mapper = {
	"0": 6,
	"1": 2,
	"2": 5,
	"3": 5,
	"4": 4,
	"5": 5,
	"6": 6,
	"7": 3,
	"8": 7,
	"9": 6
}
#Actual Numbers
mapp_num = [1,4,7,8]
unique = []
mapp = []
#`mapp` is for the Actual Numbers corresponding to its number of letters
for mp in mapp_num:
	mapp.append(mapper.get(str(mp)))
input = []
count = 0
numbars = []
with open(data_file, 'r') as f:
	for line in f:
		a,b = line.strip().split("|")
		each = b.strip().split(' ')
		every = a.strip().split(' ')
		numbar = ""
		for light in each:
			if len(light) in mapp:
				print(light)
				count+=1
			# else:
			# 	print('here is ', mapper.get(str(list(mapper.values()).index(len(light)))))
		for li in every:
			if len(li) in mapp:
				print('in input', li)
				print('which is ', list(mapper.values()).index(len(li)))
			else:
				print('unrecog', li)
		# for light in every:
		# 	if len(light) in mapp:
		# 		count+=1
		# 	else:
		# 		print(light)
			# digit = oppose_mapper.get(str(len(light)))
			# dig_set = set()
			# print(digit)
			# if isinstance(digit, list):
			# 	for char in light:
			# 		dig_set.add(char)
			# 	print('digit is ', dig_set)
			# 	for dig in digit:
			# 		char_set = set_map.get(str(dig))
			# 		print('dig is', str(dig))
			# 		print('charsets are', char_set)
			# 		if char_set == dig_set:
			# 			print(dig)
			# 			numbar+=str(dig)
			# else:
			# 	numbar+=str(digit)
		# numbars.append(numbar)

print(count)



