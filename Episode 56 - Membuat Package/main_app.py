import sains.matematika
from sains import fisika
from sains.fisika import gaya as force

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah dari package adalah = {hasil_tambah}")

gaya = fisika.gaya(90,10)
print(f"gaya adalah = {gaya}")

gaya = force(90,10)
print(f"gaya adalah = {gaya}")