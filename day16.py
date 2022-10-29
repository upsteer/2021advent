import sys

file = ""
if str(sys.argv[len(sys.argv)-1]) == 'test':
	file = "tests/"
data_file = file + "day16.txt"

with open(data_file, 'r') as f:
    input = f.read()

hex_to_bin_map = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111"
}

summed=0
summedVer=0
def get_literal_value(binary_input):
	finale = ""
	ver = int(binary_input[0:3], 2)
	type_id = int(binary_input[3:6], 2)
	# print('binn', binary_input)
	# print("header ver", ver)
	# print("header type id", type_id)
	global summed
	# global summedVer
	# summedVer+=ver
	# print(int(binary_input[0:3], 2))
	end = 0
	for num in range(6,len(binary_input), 5):
		finale+=binary_input[num+1:num+5]
		end = num
		if binary_input[num] == "0":
			end+=5
			break
	# print("literal string", finale)
	summed += int(finale, 10)
	# print(f"ended {end}")
	# print(f"summed {summed}")
	return end

# hex_inp = "D2FE28"
# hex_inp = "38006F45291200"
# hex_inp = "EE00D40C823060"
# hex_inp = "8A004A801A8002F478"
hex_inp = "620080001611562C8802118E34"
hex_inp = "C0015000016115A2E0802F182340"
hex_inp = "A0016C880162017C3686B18A3D4780"
hex_inp = "6053231004C12DC26D00526BEE728D2C013AC7795ACA756F93B524D8000AAC8FF80B3A7A4016F6802D35C7C94C8AC97AD81D30024C00D1003C80AD050029C00E20240580853401E98C00D50038400D401518C00C7003880376300290023000060D800D09B9D03E7F546930052C016000422234208CC000854778CF0EA7C9C802ACE005FE4EBE1B99EA4C8A2A804D26730E25AA8B23CBDE7C855808057C9C87718DFEED9A008880391520BC280004260C44C8E460086802600087C548430A4401B8C91AE3749CF9CEFF0A8C0041498F180532A9728813A012261367931FF43E9040191F002A539D7A9CEBFCF7B3DE36CA56BC506005EE6393A0ACAA990030B3E29348734BC200D980390960BC723007614C618DC600D4268AD168C0268ED2CB72E09341040181D802B285937A739ACCEFFE9F4B6D30802DC94803D80292B5389DFEB2A440081CE0FCE951005AD800D04BF26B32FC9AFCF8D280592D65B9CE67DCEF20C530E13B7F67F8FB140D200E6673BA45C0086262FBB084F5BF381918017221E402474EF86280333100622FC37844200DC6A8950650005C8273133A300465A7AEC08B00103925392575007E63310592EA747830052801C99C9CB215397F3ACF97CFE41C802DBD004244C67B189E3BC4584E2013C1F91B0BCD60AA1690060360094F6A70B7FC7D34A52CBAE011CB6A17509F8DF61F3B4ED46A683E6BD258100667EA4B1A6211006AD367D600ACBD61FD10CBD61FD129003D9600B4608C931D54700AA6E2932D3CBB45399A49E66E641274AE4040039B8BD2C933137F95A4A76CFBAE122704026E700662200D4358530D4401F8AD0722DCEC3124E92B639CC5AF413300700010D8F30FE1B80021506A33C3F1007A314348DC0002EC4D9CF36280213938F648925BDE134803CB9BD6BF3BFD83C0149E859EA6614A8C"
# init_bin_inp = bin(int(hex_inp, 16))[2:]
init_bin_inp = ""
for i in range(len(hex_inp)):
    init_bin_inp += hex_to_bin_map[hex_inp[i]]

# print("after padding", init_bin_inp)
# print("to ignore", to_ignore)
def get_packs(bin_inp):
	global summedVer
	# print('bn', bin_inp)
	if len(bin_inp) < 6:
		return 0
	pack_version = bin_inp[0:3]
	type_id = bin_inp[3:6]
	if not pack_version:
		return 0
	if not type_id:
		return 0
	pack_version = int(pack_version, 2)
	# print('V', pack_version)
	type_id = int(type_id, 2)
	# print(f"T {type_id}")
	length_type_id = bin_inp[6]
	summedVer+=pack_version
	skipped = 6
	if type_id == 4:
		# print("literal ret")
		skipped+=(get_literal_value(bin_inp)-6)
		return skipped
	else:
		skipped += 1
		if length_type_id == "0":
			#Length of bits to read from this packet
			till = int(bin_inp[7:22], 2)
			consumed = 0
			index = 22
			skipped += 15
			while consumed<till:
				value = get_packs(bin_inp[index+consumed:])
				if value == 0:
					break
				consumed+=value
			skipped+=till
			return skipped
		else:
			#Total no. of sub-packets in this packet
			num_of_sub = int(bin_inp[7:18], 2)
			index = 0
			value_1 = 18
			for _ in range(num_of_sub):
				calc = get_packs(bin_inp[value_1:])
				if not calc:
					break
				# print("ccaalllcc", calc)
				value_1 += calc
			skipped+=value_1
			return skipped

get_packs(init_bin_inp)
print('lastly', summed)
print('ver sum', summedVer)
