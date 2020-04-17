# membuat fungsi sederhana
def suaraayam():
    print('kukuruyuk!!!!')

def hargaayam():
    suaraayam()
    print('harga ayam per 1 kg adalah Rp. 20.000')

# membuat fungsi dengan input argumen
def hargatotalayam(kg):
    suaraayam()
    harga = 20000
    hargaTotal = kg*harga
    print('harga',kg,'kg ayam adalah',hargaTotal)

hargaayam()
hargatotalayam(2)
hargatotalayam(0.5)
hargatotalayam(1)
hargatotalayam(9)


