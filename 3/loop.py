# LOOP STATEMENTS

# Mengeksekusi suatu bagian kode secara berulang
# Looping digunakan ketika kita butuh melakukan suatu tugas secara berulang


# while loop: 
# looping berdasarkan kondisi, ini mirip dengan conditional statement (if else). 
# Tapi ada iterasi
# loop akan terus dijalankan sampai kondisinya False, baru dia keluar dari sistem looping

# for loop:
# looping berdasarkan jumlah item dalam suatu collection data type (list, tuple, set, dict, range)


# ====================================================================
# Contoh tugas yang berulang:
language = 'python'

print(f'Halo saya sedang belajar {language}')
print(f'Halo saya sedang belajar {language}')
print(f'Halo saya sedang belajar {language}')
print(f'Halo saya sedang belajar {language}')
print(f'Halo saya sedang belajar {language}') 

# Tugas di atas bisa ditulis dengan kode yang lebih ringkas
for i in range(5):
    print(f'Halo saya sedang belajar {language}')


# ====================================================================
# while loop


# Contoh 1 --------------------------------------------------------
# untuk looping angka, 

cetak = 1

while cetak <= 5:
    print(f'Halo saya sedang belajar python')

    cetak = cetak + 1

# selama nilai cetak masih <=5, maka 'Halo saya sedang belajar python' akan terus di-print
# kalau terjadi infinite loop bisa ketik ctrl+c

cetak = 1

while cetak <= 5:
    print(f'Halo saya sedang belajar python')

    cetak += 1

# cetak = cetak + 1  ------> cetak += 1


# Contoh 2 --------------------------------------------------------
# looping dengan output diprint secara horizontal 

x = 0

while x<10:
    print('x', end=' ')     # untuk print horizontal pakai end=''

    x += 1

# Contoh 3 --------------------------------------------------------
# looping maju dari -100 sampai -11

x = -100

while x < -10:
    print(x, end=' ')

    x += 1

# Contoh 4 --------------------------------------------------------
# jika while selesai (kodisinya nilainya False), maka statement else dijalankan

toko = 1

while toko <=100:
    print(f'Toko nomor {toko} ini sudah dicek')
    print('Toko belum habis')
    toko += 1
else:
    print('Semua toko sudah dicek')



# Latihan --------------------------------------------------------
# ini sendokan ke 1
# ini sendokan ke 2
# ini sendokan ke 3
# ini sendokan ke 4
# ini sendokan ke 5
# saya sudah kenyang

sendok = 1

while sendok <=5:
    print(f'ini sendokan ke {sendok}')
    sendok += 1
else:
    print('saya sudah kenyang')



# ====================================================================
# for loop
# For loop akan melakukan looping selama itemnya belum habis 


# Contoh 1 --------------------------------------------------------
# looping pada sebuah list

for item in [1,2,3,4,5]:
    print(f'ini suapan ke {item}') 


# Contoh 2--------------------------------------------------------
# looping pada range(start, stop, step)

for item in range(1,101,1):
    print(f'ini adalah suapan ke {item}')


# Latihan --------------------------------------------------------
# angka 5 adalah kelipatan 5
# angka 10 adalah kelipatan 5
# angka 15 adalah kelipatan 5
# angka 20 adalah kelipatan 5
# angka 25 adalah kelipatan 5


for angka in range(5,26,5):
    print(f'Angka {angka} adalah kelipatan 5')



# Contoh 3 --------------------------------------------------------
# looping pada range(start, stop)
# looping pada range(stop)


for item in range(1,10,2):      # range(start, stop, step)
    print(item)

for item in range(1,10):        # range(start, stop)
    print(item)

for item in range(10):          # range(stop)
    print(item)


for angka in range(5):          # item yang di-looping pada sebuah range adalah integer, sehingga bisa dilakukan operasi aritemethic seperti perkalian
    print(angka*100)




# Contoh 4 --------------------------------------------------------
# looping pada list 


for buah in ['apel','jeruk','mangga','mangga']:
    print(buah)



# Contoh 5 --------------------------------------------------------
# for loop diisi dengan if else statement

for angka in range(1,26):
    if angka%5 == 0:
        print(f'{angka} adalah kelipatan 5')
    else:
        print('Bukan kelipatan 5')


# Contoh 6 ---> unpacking


listIsiTuple = [(1,100), (2,200), (3,300)]      # tuple di dalam list

for item in listIsiTuple:
    print(item)

for depan, belakang in listIsiTuple:
    print(depan)
    print(belakang)


listIsiList = [[4,400], [5,500], [6,600]]       # list di dalam list

for i in listIsiList:
    print(i)

for i, j in listIsiList:
    print(f'{i} dikali 100 sama dengan {j}')


mobil = {'honda':'civic', 'toyota':'innova', 'mazda':'mazda2'}   # dictionary

for i in mobil:  # ouputnya hanya key nya saja
    print(i)

for i in mobil.items():
    print(i)

for brand, name in mobil.items():
    print(f'{brand} memproduksi {name}')




# Contoh 7 --------------------------------------------------------
# Kita juga dapat menggunakan for loop untuk string
# Setiap elemen pada string akan diiterasi

for huruf in 'saya belajar python':
    print(huruf)




# Contoh 8 --------------------------------------------------------
# Foor loop dengan list (salah satu collection data types)
# Kita juga bisa mengalkulasi kumpulan angka dengan multiple loops

daftar_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for angka in daftar_angka:
    total = total + angka

print(total)


for angka in daftar_angka:
    total += angka

print(total)




# Contoh 9 --------------------------------------------------------
# looping pada range jumlah item suatu list

carBrand = ['honda', 'toyota', 'ferrari', 'bmw', 'porsche', 'mazda']

for i in range(len(carBrand)):      # len(carBrand) = 6
    print(carBrand[i])





# Contoh 10 --------------------------------------------------------
# enumerate untuk menghasilkan index dan itemnya

carBrand = ['honda', 'toyota', 'ferrari', 'bmw', 'porsche', 'mazda']

for idx, name in enumerate(carBrand):
    print(idx, name)



































# ================================================================

# # SPEED, SPACE and MAINTAINABILITY

# # SPEED --> seberapa cepat kode dieksekusi 

# print('halo dunia') # 10.000 kali --> ini lebih cepat

# for i in range (10000):
#     print(i) # ini lebih lambat karena banyak step: range 1-10.000, for mengecek angka dalam range satu per satu, baru print


# # SPACE --> seberapa besar kode yang dibuat ketika disimpan. Lebih kecil lebih baik

# print('halo dunia') # 10.000 kali --> membutuhkan space pada harddisk lebih besar
# print('halo dunia')
# print('halo dunia')
# print('halo dunia')

# for i in range (10000): # membutuhkan space lebih besar pada RAM karena lebih banyak instruksi
#     print('halo dunia')


# # MAINTAINABILITY --> seberapa mudah di-maintain, misal untuk update atau debugging

# print('halo dunia') # 10.000 kali
# print('halo dunia')
# print('halo dunia')
# print('halo dunia')

# x = 'halo dunia' # lebih mudah dimaintain
# print(x)

# for i in range (10000): # ini juga mudah dimaintain
#     print('halo dunia')


# # Kalau bikin code, usahakan cari yang paling seimbang antara speed, space, dan maintainability-nya. Tapi tergantung dengan kebutuhan juga.
