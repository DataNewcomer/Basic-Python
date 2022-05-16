# # SOAL DARI SLIDE
# # =================================================================
# Soal 1
# Buat input angka dan print apakah angka tersebut bilangan genap atau ganjil.

# angka = int(input('Masukkan angka: '))

# if angka%2 == 0:
#     print(f'{angka} adalah bilangan genap')
# else:
#     print(f'{angka} adalah bilangan ganjil')




# # =================================================================
# Soal 2
# Buat user input untuk massa badan dan tinggi badan.
# Bulatkan IMT 1 angka dibelakang koma


# massa = int(input('Masukkan massa badan: '))
# tinggi = int(input('Masukkan tinggi badan: '))

# imt = massa/(tinggi/100)**2
# imt = round(imt,1)
# print('IMT anda', imt)

# if imt < 18.5:
#     print('berat badan kurang')
# elif imt < 24.9:
#     print('berat badan ideal')
# elif imt < 29.9:
#     print('berat badan berlebih')
# elif imt < 39.9:
#     print('berat badan sangat berlebih')
# else:
#     print('berat badan obesitas')



# # =================================================================
# Soal 3

# jmlApel = int(input('Masukkan jumlah apel: '))
# jmlJeruk = int(input('Masukkan jumlah jeruk: '))
# jmlAnggur = int(input('Masukkan jumlah anggur: '))

# # Diketahui harga buah sebagai berikut:
# hargaApel = 10000
# hargaJeruk = 15000
# hargaAnggur = 20000

# print('Detail Belanja')

# print(f'Apel: \t {jmlApel} x {hargaApel} = {jmlApel*hargaApel}')
# print(f'Jeruk: \t {jmlJeruk} x {hargaJeruk} = {jmlJeruk*hargaJeruk}')
# print(f'Anggur:\t {jmlAnggur} x {hargaAnggur} = {jmlAnggur*hargaAnggur}')

# totalBelanja = (jmlApel*hargaApel) + (jmlJeruk*hargaJeruk) + (jmlAnggur*hargaAnggur)
# print(f'Total belanjaan Anda Rp.{totalBelanja}')

# bayar = int(input('Masukkan jumlah uang Anda: '))

# if bayar > totalBelanja:
#     print('Terima kasih')
#     print(f'Uang kembalian Anda: {bayar-totalBelanja}')
# elif bayar == totalBelanja:
#     print('Terima kasih')
# else:
#     print('Transaksi Anda dibatalkan')
#     print(f'Uang Anda kurang: {totalBelanja-bayar}')



# # =================================================================
# Soal 4

# listA = [True, 13, 'Hello', 2.7] 
# buatlah program untuk mengetahui tipe data dari tiap item dengan menggunakan conditional if
# buat user input berisi index dari listA ('Masukkan index:')
# contoh output:
# - True bertipe data boolean
# - 2.7 bertipe data float

# index = 1

# listA = [True, 13, 'Hello', 2.7] 

# item = listA[index]
# tipe = type(item)

# # print(tipe)

# if tipe == str:
#     print(f'{item} bertipe data string') 
# elif tipe == bool:
#     print(f'{item} bertipe data boolean') 
# elif tipe == int:
#     print(f'{item} bertipe data integer') 
# elif tipe == float:
#     print(f'{item} bertipe data float')


# if type(listA[index]) == str:
#     print(f'{listA[index]} bertipe data string') 
# elif type(listA[index]) == bool:
#     print(f'{listA[index]} bertipe data boolean') 
# elif type(listA[index]) == int:
#     print(f'{listA[index]} bertipe data integer') 
# elif type(listA[index]) == float:
#     print(f'{listA[index]} bertipe data float') 




# # =================================================================
# Soal 5

# masukkan angka antara 1-99
# jika x adalah bilangan puluhan, munculkan 'x adalah puluhan'. 
# kemudian jika bilangan puluhan tersebut genap, munculkan 'x adalah bilangan genap'
# kemudian jika bilangan puluhan tersebut ganjil, munculkan 'x adalah bilangan ganjil'
# jika x adalah bilangan satuan, cukup munculkan 'x adalah satuan'
# coba gunakan range()

# contoh:
# input: masukkan angka antara 1-99: 72
# output: 
# x adalah puluhan
# x adalah bilangan genap

# input: masukkan angka antara 1-99: 9
# output: 
# x adalah satuan


# x = 5

# if x in range(10, 100): # 10,11,12,13, ...., 97,98,99
#     print('x adalah puluhan')

#     if x % 2 == 0:
#         print('x adalah bilangan genap')
#     else:
#         print('x adalah bilangan ganjil')

# else:
#     print('x adalah satuan')



# x = int(input('Masukkan angka 1-99: '))

# if x in range(10, 100, 2): # 10,12,14,....,96,98
#     print('x adalah puluhan')
#     print('x adalah bilangan genap')

# elif x in range(11, 100, 2): # 11,13,15,.....,97,99
#     print('x adalah puluhan')
#     print('x adalah bilangan ganjil')

# else:
#     print('x adalah satuan')