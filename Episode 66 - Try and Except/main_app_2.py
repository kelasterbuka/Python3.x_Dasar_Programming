# contoh membuat exception

from numbers import Number

def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "input harus angka"
    return a+b

print(tambah(5,6))

angka = 0

# try:
#     hasil = 10/angka
# except Exception as error_message:
#     print(error_message)

try:
    hasil = 10/angka
except ZeroDivisionError as error_message:
    print(error_message)