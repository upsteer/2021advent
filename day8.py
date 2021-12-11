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
duplicates = {
	"6": [0,6,9],
	"5": [2,3,5]
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
sum = 0
with open(data_file, 'r') as f:
	for line in f:
		digit = ""
		a,b = line.strip().split("|")
		each = b.strip().split(' ')
		every = a.strip().split(' ')
		unrecog = []
		digits = {}

		for li in every:
			if len(li) in mapp:
				temp = str(list(mapper.values()).index(len(li)))
				# digit+=temp
				digits[temp] = set(li)
				# print("digit is", temp)
				# print("len is", len(li))
			else:
				if not digits.get(str(len(li))):
					digits[str(len(li))] = []
				digits[str(len(li))].append(set(li))

		five = digits.pop("5")
		six = digits.pop("6")
		for index, coll in enumerate(six):
			if coll.issuperset(digits.get("4")):
				digits["9"] = coll
				continue
			if not coll.issuperset(digits.get("1")):
				digits["6"] = coll
				continue
			else:
				digits["0"] = coll
				continue

		for index_i, num in enumerate(five):
			if digits["6"].issuperset(num):
				digits["5"] = num
				continue
			if num.issuperset(digits.get("1")):
				digits["3"] = num
				continue
			else:
				digits["2"] = num
				continue

		for light in each:
			for dig in digits:
				if digits[dig] == set(light):
					digit+=str(dig)
			if len(light) in mapp:
				count+=1
			else:
				unrecog.append(light)

		print(int(digit))
		sum+=int(digit)
				

print("part 1", count)
print("part 2", sum)



