# x = 100

# def jumlah(angkaA, angkaB):
#     hasil = angkaA + angkaB + x        # hasil --> variabel local
#     return hasil

# print(jumlah(10,2))

# print(hasil)              # Error karena variable hasil adalah local variaabel dari fucntion jumlah 


# def kali(angkaC, angkaD):
#     perkalian = angkaC * angkaD * x
#     return perkalian

# print(kali(5,7))
# print(perkalian)


# =====================================================================================
# GLOBAL VARIABLE
# - Variable yang didefinisikan di luar function.
# - Global variabel memeiliki cakupan global, berarti memegang nilai/value sepanjang program dijalankan 
# - Global variable dapat diakses dis eluruh program oleh function apapun yang terdapat dalam program

# def coba():
#     print(x+2)              # 7
#     return x+3

# x = 5

# print(coba())               # 8
# print(x)                    # 5



# =====================================================================================
# LOCAL VARIABLE
# - Variebel yang didefinisikan di dalam function/blok kode
# - Local varible hanya bisa digunakan di dalam function di mana variabel tersebut didefiniskan
# - Local varible akan ada selama function dijalankan, setelah itu local variabel akan hilang/hangus secara otomatis.

# def coba():
#     x = 100
#     print(x+2)              # 102 ---> menggunakan local variable
#     return x+3

# x = 5

# print(coba())               # 103 ---> menggunakan local variable
# print(x)                    # 5   ---> menggunakan global variable



# =====================================================================================

# Error
# def coba():
#     x = x+10            # Error
#     print(x+2)
#     return x+3

# x = 5

# print(coba())
# print(x)


# # Soulusi 1: memberikan local variabel di dalam function
# def coba():
#     x = 5               # ini local variable
#     x = x+10            # x = 5+10
#     print(x+2)
#     return x+3

# x = 5

# print(coba())           # 18 --> x dari local variable
# print(x)                # 5  --> x dari global variable


# Soulusi 2: menambahkan keyword global di depan variabel
# def coba():
#     global x            # mengambil nilai x dari global variable 
#     x = x+10            # x = 5+10
#     print(x+2)
#     return x+3

# x = 5

# print(coba())           # 18 --> x dari local variable
# print(x)                # 15 --> nilai x yang awalnya 5 karena di dalam function coba ditambahkan 10, jadi nilai x berubah menjadi 15




# =====================================================================================
# CALL BACK FUNCTION
# - Function yang menerima argumen berupa function lainnya

# def tambah(angkaA, angkaB):
#     hasilTambah = angkaA + angkaB
#     return hasilTambah

# def kurang(angkaC, angkaD):
#     hasilKurang = angkaC - angkaD
#     return hasilKurang


# def matematika(func, numberA, numberB):
#     hasilMatematika = func(numberA, numberB)
#     return hasilMatematika

# print(matematika(tambah, 100, 5))
# print(matematika(kurang, 100, 5))




# =====================================================================================
# CALLING OTHER FUNCTION
# Function yang digunakan di dalam function lainnya

# def tampilkan(jawaban):
#     print(f'Jawabannya adalah {jawaban}')

# # tampilkan(90)

# def perkalian(angkaX, angkaY):
#     hasil = angkaX * angkaY
#     tampilkan(hasil)

# perkalian(7, 10)



# =====================================================================================
# LAMBDA FUNCTION
# - Function kecil yang tidak punya nama
# - Bisa punya beberapa parameter, tapi hanya punya 1 expression/statement
# - Syntax --> lambda parameter: expression

# kuadrat = lambda angka: angka**2  
# print(kuadrat(5))

# perkalian = lambda angkaA,angkaB: angkaA*angkaB
# print(perkalian(6,7))



# =====================================================================================
# MAP
# - Digunakan untuk mengubah nilai atau bentuk dari data-data yang ada di collection data types 
#   tanpa mengubah banyak/jumlah datanya

listA = [1,2,3,4]

# def kuadrat(angka):
#     return angka**2

# list_baru = []

# for i in listA:
#     list_baru.append(kuadrat(i))

# print(list_baru)

# ----------------------------------------------------------------------
# Cara yang biasa kita gunakan dengan looping
# listA = [1,2,3,4]

# def kuadrat(list_angka):

#     list_baru = []              # 1 4 9 16
#     for i in list_angka:
#         list_baru.append(i**2)

#     return list_baru

# print(kuadrat(listA))


# ----------------------------------------------------------------------
# Cara menggunakan map
# Syntax --> map(function, list)
# Hasilnya dalam betuk map object
# diubah menjadi list agar hasilnya ditampilkan dalam betuk list

# listA = [1,2,3,4]

# def kuadrat(angka):
#     return angka**2

# print(list(map(kuadrat, listA)))            # functionnya menggunakan regular function

# print(list(map(lambda x: x**2, listA)))     # functionnya menggunakan lambda function


# Latihan ----------------------------------------------------------------------

# tarif taxi per kilometer adalah 5000
# awal buka pintu sudah dikenakan tarif 8000
# berapa tarif taxi untuk perjalanan sejauh 1, 2, 3, 4, dan 5 kilometer
# tampilkan dalam list


# kilometer = [1,2,3,4,5]

# # Menggunakan regular function
# def tarif(jarak):
#     return (jarak*5000)+8000

# print(list(map(tarif, kilometer)))


# # Menggunakan lambda function
# print(list(map(lambda jarak: (jarak*5000)+8000, kilometer)))


# # Menggunakan list comprehension
# # Syntax --> [output for item in list]
# print([(jarak*5000)+8000 for jarak in kilometer])


# =====================================================================================
# FILTER
# - Digunakan untuk filtering (memilih) data pada collcetion data types
# - Jumlah item dalam list akan berkurang karena difilter
# - Item tidak berubah

# kilometer = [1,2,3,4,5]

# def genap(angka):
#     if angka%2==0:
#         return True
#     else:
#         return False

# print(genap(7))


# # Tidak pakai filter (looping manual)
# kilometer = [1,2,3,4,5]

# list_genap = []

# for angka in kilometer:
#     if angka%2==0:
#         list_genap.append(angka)

# print(list_genap)


# # filter menggunakan regular function
# kilometer = [1,2,3,4,5]

# def genap(angka):
#     return angka%2 == 0

# print(genap(9))

# print(list(filter(genap, kilometer)))


# # filter menggunakan lambda
# print(list(filter(lambda angka: angka%2==0, kilometer)))


# Latihan Map ----------------------------------------------------------------------

# Buatlah function dengan input dan output seperti contoh di bawah ini
# [1,3,4,5]         --> ['Ganjil', 'Ganjil', 'Genap', 'Ganjil']
# [22,17,19,20,14]  --> ['Genap', 'Ganjil', 'Ganjil', 'Genap', 'Genap']
# [1,3,5]           --> ['Ganjil', 'Ganjil', 'Ganjil']
# [2,4,6]           --> ['Genap', 'Genap', 'Genap']


# list_bilangan = [1,3,4,5]

# # Cara map dgn regular function
# def ganjil_genap(angka):
#     if angka%2==0:
#         return 'Genap'
#     else:
#         return 'Ganjil'

# print(list(map(ganjil_genap, list_bilangan)))


# # Cara map dgn lambda function
# Syntax --> lambda parameter: output_True if statement True else output_False
# print(list(map(lambda angka: 'Genap' if angka%2==0 else 'Ganjil', list_bilangan)))


# # Cara list comprehension
# Syntax --> [output_True if statement True else output_False for item in list]
# print(['Genap' if angka%2==0 else 'Ganjil' for angka in list_bilangan])


# # Looping biasa
# list_string = []
# for angka in list_bilangan:
#     if angka%2==0:
#         list_string.append('Genap')
#     else:
#         list_string.append('Ganjil')

# print(list_string)




# Latihan Filter ----------------------------------------------------------------------

# Buatlah sebuah function untuk melakukan filtering pada suatu list berisi gaji karyawan.
# Tampilkan gaji yang tetap berniai di atas 9 juta setelah dikurangi 5% dari gaji tersebut 
# listGaji = [9100000, 9800000, 9500000, 10300000, 9300000]

# cara 1: regular function
# listGaji = [9100000, 9800000, 9500000, 10300000, 9300000]

# def over9juta(gaji):
#     if gaji - (gaji*(5/100)) > 9000000:
#         return True
#     else:
#         return False

# def filter9juta(fn, my_list):
#     filtering = list(filter(fn, my_list))
#     return filtering

# print(filter9juta(over9juta, listGaji))


# cara 2: lambda function
# def filter9million(my_list):
#     filtering = list(filter(lambda gaji: gaji-(gaji*(5/100)) > 9000000, my_list))
#     return filtering

# listGaji = [9100000, 9800000, 9500000, 10300000, 9300000]

# print(filter9million(listGaji))



# # =========================================================================
# Recursive Function
# Sebuah function memanggil dirinya sendiri di dalam function tersebut


# def countdown(counter):
#     print(counter)
#     counter -= 1

#     if counter >= 0:
#         countdown(counter)
#         print(f'counter = {counter}')

# countdown(3) 







