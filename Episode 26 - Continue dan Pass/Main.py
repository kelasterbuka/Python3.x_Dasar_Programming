# continue, pass, break

# pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi

# angka = 0

# while angka < 5:
# 	angka += 1

# 	if angka == 3:
# 		pass # ini tidak akan dieksekusi

# 	print(angka)

# continue

angka = 0

print(f"angka sekarang -> {angka}")

while angka < 5:
	angka += 1
	print(f"angka sekarang -> {angka}") # aksi 1

	if angka == 3:
		print("nice!")
		continue # akan membuat loop meloncat ke step selanjutnya

	print("whassup!") # aksi 2

print("Pinish!")