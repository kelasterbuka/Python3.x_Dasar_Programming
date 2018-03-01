# scope variable : global

namaKucing = 'cassandra'
makananKucing = 'royal canin'

def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru # variable global
    nama = namaBaru # variable local
    print('saya rubah nama kucing menjadi',namaKucing)

def kasihMakanKucing(makanan,nama):
    global namaKucing,makananKucing
    namaKucing = nama
    makananKucing = makanan

rubahNamaKucing('ketie')

kasihMakanKucing('universal','alex')

print('nama kucing saya menjadi',namaKucing,'dan makan',makananKucing)