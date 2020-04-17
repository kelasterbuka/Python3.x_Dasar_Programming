# fungsi dengan menggunakan argumen sederhana
def siswa(nama):
    print('siswa ini bernama:',nama)

siswa('mario')

# fungsi dengan menggunakan keywords arguments

def guru(nama,pelajaran):
    print('guru ini bernama:',nama)
    print('mengajar:',pelajaran)

guru(nama='popong',pelajaran='seni rupa')
guru(pelajaran='olah raga',nama='endang')
guru('olah raga','raihan') # ini contoh yang salah

# fungsi dengan menggunakan default arguments

def penjagaSekolah(nama,shift='siang',galak='tidak'):
    print('penjaga sekolah ini bernama:', nama)
    print('shiftnya:', shift)
    print('galak?:', galak)

penjagaSekolah('Entis')
penjagaSekolah('Maman',shift='malam')
penjagaSekolah('Asep',galak='Sangat')
penjagaSekolah(shift='malam',galak='iya') # menghasilkan error




