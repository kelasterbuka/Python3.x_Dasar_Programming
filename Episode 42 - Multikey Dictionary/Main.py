import datetime

mahasiswa1 = {
	'nama':'Ucup Surucup',
	'nim':'19022001',
	'sks_lulus':130,
	'beasiswa':False,
	'lahir':datetime.datetime(2001,4,10)
}

mahasiswa2 = {
	'nama':'Otong Surotong',
	'nim':'19022002',
	'sks_lulus':140,
	'beasiswa':True,
	'lahir':datetime.datetime(2002,10,10)
}

mahasiswa3 = {
	'nama':'Asep Si Kasyep',
	'nim':'19022003',
	'sks_lulus':100,
	'beasiswa':False,
	'lahir':datetime.datetime(2000,2,29)
}

data_mahasiswa = {
	'MAH001':mahasiswa1,
	'MAH002':mahasiswa2,
	'MAH003':mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
	KEY = mahasiswa

	NAMA = data_mahasiswa[KEY]['nama']
	NIM = data_mahasiswa[KEY]['nim']
	SKS = data_mahasiswa[KEY]['sks_lulus']
	BEASISWA = data_mahasiswa[KEY]['beasiswa']
	LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

	print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
