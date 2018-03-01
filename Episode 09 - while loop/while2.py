# else, break, continue, pass

angka = 0

while angka < 10:

    if angka is 5:
        # print('checkpoint 1')
        break
        continue
        pass
        # print('checkpoint 2')

    print( 'nilai angka adalah:', angka)
    angka += 1
else:
    print('nilai angka diakhir while adalah',angka)

print('di luar while')