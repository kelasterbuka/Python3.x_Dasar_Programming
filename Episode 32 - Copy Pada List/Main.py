## Teknik menduplikat list

a = ["Ucup","Otong","Dudung"]
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")

# kita akan merubah member dari a

# ini akan merubah kedua list
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikat list dengan copy

print("membuat list c dengan a.copy()")
c = a.copy() # full duplikat / data baru

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Kita ubah data 0")
c[0] = "Dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Kita ubah data 1")
a[1] = "Otong"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")