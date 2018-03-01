# class
class mahasiswa():

    jumlah_mahasiswa = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama # public
        self.nim = input_nim  # public
        mahasiswa.jumlah_mahasiswa += 1

# main programnya

otong = mahasiswa("otong surotong", 13317001)
ucup = mahasiswa("michael ucup", 13317002)
cassandra = mahasiswa("cassandra aja", 13317002)

print(mahasiswa.jumlah_mahasiswa)
