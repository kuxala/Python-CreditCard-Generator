import random 
def char_12():
	char_12 = []
	for i in range(0,13):
		char_12.append(i)
	# return char_12
	rand_char_2 = []
	for j in range(0,10):
		rand_char = random.choice(char_12)
		rand_char_2.append(rand_char)
	str_char = str(rand_char_2)
	str_char = str_char.replace(" ", "")
	str_char = str_char.replace(",", "")
	return "12 digits: " + str_char


def char_3():
	rand = []
	for i in range(1,4):
		rand.append(i)

	rand_char_1 = []
	for j in range(1,4):
		rand_char = random.choice(rand)
		rand_char_1.append(rand_char)
	str_rand_char = str(rand_char_1)
	str_rand_char = str_rand_char.replace(",", "")
	str_rand_char = str_rand_char.replace(" ", "")
	return "3 digits: " + str_rand_char

def date():
	first = []
	for i in range(1,12):
		first.append(i)
	
	second = []
	for j in range(1,31):
		second.append(j)

	for i in range(0,2):
		rand_first = random.choice(first)
		rand_second = random.choice(second)
		str_first = str(rand_first)
		str_second = str(rand_second)
	return "date: " + str_first + "/" + str_second

print(char_12())
print(char_3())
print(date())