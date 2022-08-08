# module matematika dengan import

from matematika import tambah as add
from matematika import kali as k
from matematika import pangkat as terserah_kalian_mau_apa
# from matematika import *

import matematika as math # <--- bisa dilakukan

hasil_tambah = add(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = math.kali(1,2,3,4,5)
print(f"hasil tambah = {hasil_kali}")

pangkat_3 = terserah_kalian_mau_apa(3)
print(f"hasil pangkat3 = {pangkat_3(3)}")