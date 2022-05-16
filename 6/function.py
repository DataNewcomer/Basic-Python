# FUNCTION

# Function adalah sebuah blok kode terorganisir yang dapat menerima input dan mengeluarkan output, dan dapat digunakan berulang kali. 
# Jika suatu proses dilakukan berulang kali, maka kita bisa gunakan function.
# Function bisa digunakan di banyak tempat berbeda, agar tidak perlu copy paste
# Function bisa digunakan oleh orang lain, tanpa harus orang lain tsb tau bagaimana proses di dalam functionnya.
# Function secara umum punya input dan output.
# Built-in function adalah funtion bawaan dari python


# # Regular function
# def tambah(angkaA, angkaB):         # def nama_function(parameter, parameter)
#     return angkaA + angkaB          #      return return_value

# # Memanggil function
# print(tambah(3,5))                  # nama_function(argumen, argumen)


# # Lambda function
# # Function tanpa nama
# lambda angkaA,angkaB: angkaA+angkaB


# ==========================================================================================
# Function tanpa input dan tanpa output

# def salam():
#     print('Selamat Pagi')
#     print('Kita akan belajar function di python')

# salam()


# Latihan ------------------------------------------------------------------------

# Buat function untuk menampilkan teks di bawah ini.
# output: 
# Halo, selamat datang di Toko Kami
# Jam operasional:
# Senin - Jumat: 08.00 - 21.00
# Sabtu - Minggu: Libur
# Pesanan dikirim setiap jam 3 sore, lewat jam 3 sore pesanan di kirim besoknya.

# def olshop():
#     print('Halo, selamat datang di Toko Kami.')
#     print('Jam operasional:')
#     print('Senin - Jumat: 08.00 - 21.00')
#     print('Sabtu - Minggu: Libur')
#     print('Pesanan dikirim setiap jam 3 sore, lewat jam 3 sore pesanan di kirim besoknya.')

# olshop()



# ==========================================================================================
# Function dengan input tapi tanpa output

# def nama_function(parameter, parameter) --> apa yang harus diinput
# def perkenalan(nama, umur):
#     print(f'Halo nama saya {nama} dan umur saya {umur} tahun')
#     print('Senang berkenalan dengan teman-teman')

# nama_function(argumen, argumen) --> apa yang diinput ke dalam parameter
# perkenalan('Tony', 20)

# jangan kebalik urutannya kalau tidak menyebutkan parameter
# perkenalan(20, 'Tony') 

# bisa tidak beururtan, tapi harus sebut parameternya
# perkenalan(umur=20, nama='Tony')


# Latihan ------------------------------------------------------------------------

# Buatlah function bernama 'oscar' dengan parameter berupa nama actor, film, dan tahunnya.
# output:
# Pemenang Aktor Terbaik tahun 2016 adalah Leonardo DiCaprio pada film "The Revenant"

# def oscar(year, actor, movie):
#     print(f'Pemenang Aktor Terbaik tahun {year} adalah {actor} pada film "{movie}"')

# oscar(2016, 'Leonardo DiCaprio', 'The Revenant')
# oscar(actor='Leonardo DiCaprio', movie='The Revenant', year=2016)



# ==========================================================================================
# Function dengan input dan dengan output

# def kuadrat(angka):
#     hasilKuadrat = angka**2
#     return hasilKuadrat             # return value (output) berupa integer

# print(kuadrat(5))


# def tambah(angkaA, angkaB):
#     hasilTambah = angkaA + angkaB
#     return hasilTambah              # return value berupa integer

# print(tambah(9, 10))
# print(kuadrat(6) * tambah(8,2))     # integer * integer = integer


# # Hati-hati kalau pakai print (bukan pakai return)
# def kuadrat(angka):
#     hasilKuadrat = angka**2
#     print(hasilKuadrat)             # ini bukan return value (output) 

# print(kuadrat(5))                   # hasil print yang diprint lagi akan menghailkan None
# print(kuadrat(6) * tambah(8,2))     # None * integer = Error


# Latihan ------------------------------------------------------------------------

# Buatlah function untuk menghitung luas lingkaran dengan parameter berupa radius

# import math

# def lingkaran(radius):
#     luas = math.pi * (radius**2)
#     return luas

# print(lingkaran(10))
# print(lingkaran(5)*100)



# ==========================================================================================
# Default Parameter
# Jika tidak memasukkan argumen saat function dipanggil, functionnya sudah memiliki nilai default untuk parameter tersebut


# def tambah(angkaA=0, angkaB=100):
#     hasilTambah = angkaA + angkaB
#     return hasilTambah              

# print(tambah(9))              # Error kalau cuma input 1 argumen


# def perkenalan(nama='Unknown', umur=0, tinggal='Unknown'):
#     if (nama!='Unknown') and (umur>0):
#         print(f'Halo nama saya {nama} dan umur saya {umur} tahun')
#     elif (nama!='Unknown') and (umur==0):
#         print(f'Halo nama saya {nama}')
#     elif (nama=='Unknown') and (umur>0):
#         print(f'Halo umur saya {umur} tahun, saya ga mau sebutin nama')
#     else:
#         print(f'Saya ga mau memperkenalkan diri')


# perkenalan()
# perkenalan('Alex', 25)
# perkenalan(umur=25, nama='John')
# perkenalan('Paul')
# perkenalan(40)
# perkenalan(umur=40)



# ==========================================================================================
# Exercise
# ==========================================================================================

# Soal 1

# tarif taxi per kilometer adalah 5000
# awal buka pintu sudah dikenakan tarif 8000
# berapa tarif taxi untuk perjalanan sejauh 1, 2, 3, 4, dan 5 kilometer
# tampilkan dalam list


# kilometer = [1,2,3,4,5]

# def tarif(listJarak):
    
#     total = []
#     for x in listJarak:
#         jarak = (x*5000) + 8000
#         total.append(jarak)

#     return total

# print(tarif(kilometer))

# kilometer = [1,2,3]

# def hargaTaxi(listJarak):

#     tarif = []
#     for i in listJarak:
#         hasil = (i * 5000) + 8000
#         tarif.append(hasil)

#     return tarif

# print(hargaTaxi(kilometer))



# ==========================================================================================
# Soal 2

# buat function dengan parameter yang akan diisi dengan argumen berupa sebuah kalimat, contoh
# argumen: teh cukup murah
# output: teh pukuc harum

# syarat: 
# hanya kata yg memiliki panjang lebih dari 3 huruf yang dibalik
# input hanya berupa huruf dan spasi, tanpa tanda baca

# sugestion: pakai looping string dan list
# pakai conditional if


# ----------------------------------
# cara1
# def terbalik(kalimat):

#     listKalimat = kalimat.split(' ') # ['teh','cukup','murah]

#     for i in listKalimat:            # 'teh'      

#         for j in range(len(i)):           # range(0,3) --> 0 1 2   

#             if len(i)>3:                      # index       -->  2   1   0
#                 flip = i[len(i)-1-j]          # 'teh'[3-1-0] --> 'h' 'e' 't'
#                 print(flip, end='')
#             else:
#                 biasa = i[j]                  # 'teh'[0]     --> 't' 'e' 'h'        
#                 print(biasa, end='')

#         print(' ', end='')                # buat spasi setelah looping j selesai (spasi setiap kata)

# terbalik('teh cukup murah')



# ----------------------------------
# cara2
# def kebalik(kalimat):
    
#     listKalimat = kalimat.split(' ')      # hasil split --> ['pagi', 'ini', 'lumayan', 'panas']

#     for i in listKalimat:
#         if len(i) > 3:
#             print(i[::-1], end=' ')     
#         else:
#             print(i, end=' ')

# kebalik('pagi itu lumayan panas')


# ==========================================================================================
# Soal 3

# Buat algoritma untuk memutar list di dalam list yang berukuran 3x3 satu kali searah jarum jam.
# misal:
# input
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]

# output
# [[7,4,1],
#  [8,5,2],
#  [9,6,3]]    

# --------------------------------------------------------------------
# cara 1
# pakai indexing dan for loop

# listA = [[1,2,3], [4,5,6], [7,8,9]]

# def rotate(list_angka): # buat fungsi bernama rotate
    
#     # for loop dalam fungsi
#     listB = []                        #  []
#     for i in range(0,3):              #  0 1 2

#         listC = []                              # [7,4,1]             
#         for j in range(2,-1,-1):                # 2 1 0
#             listC.append(list_angka[j][i])      # 

#         listB.append(listC)

#     return (listB) # jika fungsi rotate dijalankan, maka akan ngeprint isi list3 (list1 yg telah berputar)

# print(rotate(listA)) # fungsi rotate digunakan pada list1

# print()

# # --------------------------------------------------------------------
# # cara 2

# mylist = [[1,2,3], 
#           [4,5,6], 
#           [7,8,9]]


# def rotate(list_number):
#     unpack_list = list(zip(*list_number))

#     outer = []                  # [[7,4,1]
#     for i in unpack_list:       # (1,4,7) 

#         inner = []                                      # [7,4,1]
#         for j in range(len(list_number)-1,-1,-1):       # 3 2 1 0
#             inner.append(i[j])

#         outer.append(inner)

#     return outer

# print(rotate(mylist))

# # ----------------------------------
# # cara 3

# mylist = [[1,2,3], [4,5,6], [7,8,9]]


# def rotasi(list_angka):
#     outer = []                          # [[7,4,1], [8,5,2]]

#     for i in zip(*list_angka):          # (1,4,7) (2,5,8)
#         outer.append(list(i[::-1]))     # (7,4,1) --> [7,4,1]

#     return outer

# print(rotasi(mylist))



