# input output file



"""
w = write mode / mode menulis dan menghapus file lama, jika file tidak ada maka akan dibuat file baru
r = read mode only / hanya bisa baca
a = appending mode / menambahkan data di akhir baris
r+ = write and read mode

"""
# membuat file text

file = open("data.txt",'w')

file.write("ini adalah data text yang dibuat dengan menggunakan python")
file.write("\nini baris kedua")
file.write("\nini baris ketiga")
file.write("\nini baris keempat")

file.close()

# membaca file text

file2 = open("data.txt",'r')

#print(file2.read(10))

print(file2.readline())

file2.close()


# appending mode

file3 = open("data.txt", 'a')

file3.write("\nbaris ini dibuat dengan menggunakan mode append")

file3.close()

