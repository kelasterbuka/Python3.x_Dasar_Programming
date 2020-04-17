# class
class mahasiswa():

    jurusan = "teknik tata boga"
    __nilai = 0 # private

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama # public
        self.nim = input_nim  # public

    def uts(self,input_nilai):
        self.__nilai += input_nilai

    def uas(self,input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama,'tidak lulus')
        else:
            print(self.nama, 'lulus')

# main programnya

otong = mahasiswa("otong surotong", 13317001)
ucup = mahasiswa("michael ucup", 13317002)

otong.uts(10)
otong.uas(50)
otong.check_status()
ucup.uts(5)
ucup.uas(25)
ucup.__nilai = 60
ucup.check_status()
