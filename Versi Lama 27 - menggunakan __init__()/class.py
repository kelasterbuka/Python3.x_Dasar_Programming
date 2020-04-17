#class
class Mahasiswa():
	nama = 'nama'

	def __init__(self, input_nama, input_nim):
		self.nama = input_nama
		self.nim = input_nim

	def belajar(self, kondisi):
		print(self.nama,'sedang belajar', kondisi)

	def tidur(self):
		print(self.nama,'tidur di kelas')

# main programnya

otong = Mahasiswa("otong surotong", 13317001)
#ucup = Mahasiswa()

print(otong.nama)
otong.nama = "atong suratang"
print(otong.nama)

#ucup.nama = "michael ucup"
otong.belajar('dengan giat')
#ucup.tidur()