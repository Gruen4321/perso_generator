#! /usr/bin/python3

import random

random.seed(None)

birth_year = int(input("Birth year: "))
birth_month = int(input("Birth month: "))
birth_day = int(input("Birth day: "))

exp_year = int(input("Expirency year: "))
exp_month = int(input("Expirency month: "))
exp_day = int(input("Expirency day: "))

def checksum(arr):
	ret = 0
	mode = 7
	for x in arr:
		ret += mode * x
		if mode == 7:
			mode = 3
		elif mode == 3:
			mode = 1
		else:
			mode = 7
	return ret % 10

def rand():
	return random.randrange(9)

# Generate ID 1
id_1 = []

# Add German BKZ
id_1.extend([6, 3, 9, 6])

# Generate random numbers
for i in range(0, 5):
	id_1.append(rand())

# Generate checksum
id_1.append(checksum(id_1))

# Generate ID 2
id_2 = []

# Birth year
id_2.append(int(birth_year / 10))
id_2.append(birth_year % 10)

# Birth month
id_2.append(int(birth_month / 10))
id_2.append(birth_month % 10)

# Birth day
id_2.append(int(birth_day / 10))
id_2.append(birth_day % 10)

# Generate checksum
id_2.append(checksum(id_2))

# Generate ID 3
id_3 = []

# Expirency year
id_3.append(int(exp_year / 10))
id_3.append(exp_year % 10)

# Expirency month
id_3.append(int(exp_month / 10))
id_3.append(exp_month % 10)

# Expirency day
id_3.append(int(exp_day / 10))
id_3.append(exp_day % 10)

# Generate checksum
id_3.append(checksum(id_3))

# Generate complete checksum
cksum = checksum(id_1 + id_2 + id_3)

# Output results
print("")
print("ID 1: ", *id_1, sep="")
print("ID 2: ", *id_2, sep="")
print("ID 3: ", *id_3, sep="")
print("Checksum: ", cksum)
