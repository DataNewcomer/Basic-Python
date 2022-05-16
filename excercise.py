# ======================================================================================
# No. 1
# Print hanya angka yang bisa dibagi 3 dari list_angka
# list_angka =[15,2,4,45,7,23,47]

# list1=[15,2,4,45,7,23,47]
# for i in list1:
#     if i%3 == 0:
#         print(i)




# ======================================================================================
# No. 2

# Tampilkan kata dengan mengambil 2 huruf pertama dan 2 huruf terakhir dari kata yang diinput
# input: Purwadhika
# output: Puka (2 huruf pertama dan 2 huruf terakhir dari input)

# kata = input('Masukkan kata: ')
# print(kata[:2]+kata[-2:])




# ======================================================================================
# No. 3

# Tukar tanda koma dan tanda titik dari bilangan yang diinput 
# input  "32.054,23"
# Output "32,054.23" (koma diganti titik; titik diganti koma)

# # Cara 1 -------------------------------------------------------------
# angka = input('Masukkan angka: ')
# list_angka = list(angka)
# list_angka[2], list_angka[6] = list_angka[6], list_angka[2]
# print(''.join(list_angka))

# # Cara 2 -------------------------------------------------------------
# angka = input('Masukkan angka: ')
# angka2 = angka.replace('.','a')
# print(angka2)
# angka2 = angka2.replace(',','b')
# print(angka2)
# angka2 = angka2.replace('b','.')
# print(angka2)
# angka2 = angka2.replace('a',',')
# print(angka2)




# ======================================================================================
# No. 4

# Buatlah fungsi untuk menggambar segitiga berikut berisi parameter berupa tinggi segitiga.

# misal: tinggi=4
#       *
#     * *
#   * * *    
# * * * *

# tinggi = int(input('Masukkan tinggi segitiga: '))

# Cara 1 -------------------------------------------------------------
# tinggi = int(input('Masukkan tinggi segitiga: '))

# for i in range(0, tinggi):              # 0 1 2 3
#     for j in range(tinggi-1, -1, -1):   # 3 2 1 0
#         if i<j:                         # akan membuat spasi selama i<j
#             print('  ', end='')
#         else:                           # akan membuat * selama i<j
#             print(' *', end='')
#     print()

# Cara 2 -------------------------------------------------------------
# tinggi = int(input('Masukkan tinggi segitiga: '))

# for i in range(tinggi):
#     for j in range(tinggi-(i+1)):
#         print('-', end=' ')
#     for j in range (i+1):
#         print('*', end=' ')
#     print()




# ======================================================================================
# No. 5

# dictKaryawan = {'Andi': [23, 9], 'Budi': [28, 11], 'Caca': [22, 13], 'Dedi': [27, 14], 'Elena': [34, 15]}
# Dari dictKaryawan di atas, tampilkan output untuk seluruh 5 orang karyawan tersebut.
# Contoh output:
# "Nama karyawan adalah Andi, umur 23, gaji 9 juta"
# "Nama karyawan adalah Budi, umur 28, gaji 11 juta"


# Cara 1 -------------------------------------------------------------
# dictKaryawan = {'Andi': [23, 9], 'Budi': [28, 11], 'Caca': [22, 13], 'Dedi': [27, 14], 'Elena': [34, 15]}

# for i in dictKaryawan:
#     nama = i                      # i mewakili setiap key dalam dictKaryawan
#     umur = dictKaryawan[i][0]     # indexing 23
#     gaji = dictKaryawan[i][1]     # indexing 9
#     print(f'Nama karyawan adalah {nama}, umur {umur} tahun, gaji {gaji} juta')

# Cara 2 -------------------------------------------------------------
# dictKaryawan = {'Andi': [23, 9], 'Budi': [28, 11], 'Caca': [22, 13], 'Dedi': [27, 14], 'Elena': [34, 15]}

# for key, value in dictKaryawan.items():
#     print(f'Nama karyawan adalah {key}, umur {value[0]} tahun, gaji {value[1]} juta')




# ======================================================================================
# No. 6

# Buat algoritma untuk menentukan apakah suatu bilangan adalah bilangan prima
# Contoh:
# input --> Masukkan angka: 7
# 7 adalah bilangan prima
# input --> Masukkan angka: 12
# 12 bukan merupakan bilangan prima


# angka = int(input('Masukkan angka: '))

# if angka > 1:
#     for i in range(2, angka):
#         if (angka % i) == 0:
#             print(f'{angka} bukan merupakan bilangan prima')
#             break
#     else:
#         print(f'{angka} merupakan bilangan prima')
# else:
#     print(f'{angka} bukan merupakan bilangan prima')




# ======================================================================================
# No. 7

# Buat while loop untuk mencari angka 13 di antara angka 1-100
# Print setiap angka sampai 13, ketika angka 13 ketemu, print 'HORE angka 13 ditemukan'


# x = 1
# dicari = 13

# while x <= 100:
#     print(x)

#     if x == dicari:
#         print(f'HORE angka {x} ditemukan')
#         break

#     x += 1




# ======================================================================================
# No. 8

# Buat looping dengan output:
# ini bilangan ganjil [1, 3, 5, 7, 9]
# ini bilangan genap [2, 4, 6, 8, 10]


# list_ganjil = []
# list_genap = []

# for i in range(1,11): 
#     if i %2 == 0:
#         list_genap.append(i)
#     else:
#         list_ganjil.append(i)

# print('ini bilangan ganjil', list_ganjil)
# print('ini bilangan genap', list_genap)




# ======================================================================================
# No. 9

# Gunakan looping untuk membuat list yang berisikan huruf depan dari setiap kata pada kalimat di bawah ini
# Lalu gabungkan setiap huruf depan menjadi satu kata!
# kalimat = 'Buatlah list yang berisikan huruf depan dari setiap kata pada kalimat ini'
# contoh output: Blybhddskpki

# kalimat = 'Buatlah list yang berisikan huruf depan dari setiap kata pada kalimat ini'

# hasil = []

# for kata in kalimat.split():
#     hasil.append(kata[0])

# print(''.join(hasil))




# ======================================================================================
# No. 10

# Buatlah klasifikasi kendaraan menggunakan conditional statements!
# - motor manual
# - motor automatic
# - mobil manual
# - mobil automatic

# Contoh:
# input: Masukkan nama kendaraan Anda: Ferrari
# Anda memilih Ferrari
# input: Apakah Ferrari punya 2 atau 4 roda? 4
# input: Apakah Ferrari manual atau automatic? (m/a): a
# Ferrari adalah mobil automatic


# kendaraan = input('Masukkan nama kendaraan Anda: ')
# print(f'Anda memilih {kendaraan} \n')

# roda = input(f'Apakah {kendaraan} punya 2 atau 4 roda? ')

# if roda == '2':

#     transmisi = input(f'Apakah {kendaraan} manual atau automatic? (m/a): ')
#     if transmisi == 'm':
#         print(f'{kendaraan} adalah motor manual')
#     else:
#         print(f'{kendaraan} adalah motor automatic')

# else:
#     transmisi = input(f'Apakah {kendaraan} manual atau automatic? (m/a): ')
#     if transmisi == 'm':
#         print(f'{kendaraan} adalah mobil manual')
#     else:
#         print(f'{kendaraan} adalah mobil automatic')




# ======================================================================================
# No. 11

# Output :
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# 13 14 15


# Cara 1 -------------------------------------------------------------

# for i in range(1, 16, 3):     # output --> 1, 4, 7, 10, 13)
#     for j in range(3):
#         print(i, end = ' ')
#         i += 1
#     print()                   # metode start: stop: step nya range


# Cara 2 -------------------------------------------------------------

# x = 0 
# for i in range(5):            # jumlah baris yang diperlukan
#     for j in range(0, 3):     # jumlah kolom yang diperlukan
#         x += 1
#         print(x, end = ' ')
#     print()

# Cara 3 -------------------------------------------------------------

# x = 1
# for i in range(5):            # 0 1 2 3 4 --> ini yang buat print 5 baris ke bawah
#     for j in range(3):        # 0 1 2 --> ini yang buat ngeprint 3 kali ke samping
#         print(x, end = ' ')   # print x dulu, lalu spasi ke samping
#         x += 1                # lalu looping x + 1 setelahnya
#     print()                   # ini untuk print ke bawah setelah ada 3 kolom, atau setelah loop j selesai 3x




# ======================================================================================
# No. 12

# Buatlah kode dengan looping untuk menghasilkan output seperti di bawah ini:
# 10 8 6 4 2 0

# Cara 1 -------------------------------------------------------------
# x = 12

# for i in range(x):
#     x -= 2
#     if x >= 0:
#         print(x, end = ' ')
#     else:
#         break

# Cara 2 -------------------------------------------------------------

# x = 10
# for i in range(6):
#     print(x, end = ' ')
#     x -= 2


# Cara 3 -------------------------------------------------------------

# for i in range(10, -1, -2): # start 10, stop -1, step -2
#     print(i, end = ' ')


