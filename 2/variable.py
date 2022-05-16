# Varieble

# Variable adalah sebuah fitur dalam bahasa pemrograman untuk menympan suatu nilai
# Varible bisa analogikan sebagai sebuah box
# - box tsb punya nama
# - box tsb menyimpan sebuah nilai

# siswa = 'Anton' 
# umur = 23

# print(siswa)
# print(umur)

# print(siswa, umur)

# Cara Penamaan Vaiable yg Benar

# namaSiswaKelasA = 'Billy'
# print(namaSiswaKelasA)

# nama_siswa = 'Caca'
# print(nama_siswa)

# NAMASISWA = 'Donny'
# print(NAMASISWA)

# namaSiswa3 = 'Eliza'
# print(namaSiswa3)

# _nama_siswa = 'Toby'
# print(_nama_siswa)


# Cara Penamaan Vaiable yg Salah

# 3namaSiswa = 'Frank'
# print(3namaSiswaa)

# nama siswa = 'Gallardo'
# print(nama siswa)

# nama-siswa = 'Hellena'
# print(nama-siswa)




# ================================================================================
# Data Type: tipe data dari suatu variable

# my_var = 'Frank'                # string
# my_var = 'Nama saya Frank'      # string
# my_var = '30'                   # string

# my_var = 30                     # integer
# my_var = 30.79                  # float

# my_var = True                   # boolean
# my_var = False                  # boolean

# my_var = None                   # None


# Collection Data Type

# my_var = [1,2,3,4]                          # list
# my_var = (1,2,3,4)                          # tuple
# my_var = {1,2,3,4}                          # set
# my_var = {'one':1, 'two':2, 'three':3}      # dictionary
# my_var = range(5)                           # range

# print(my_var)
# print(type(my_var))

# Latihan 1
# angka = ['12']
# angka = '12'
# angka = 12

# print(angka)
# print(type(angka))

# Latihan 2
# Buat dictionary berisi 3 item, key-nya adalah kata bahasa inggris, valuenya adalah terjemahan bahasa indonesia!
# dictA = {'cat':'kucing', 'dog':'anjing', 'bird':'burung'}

# print(dictA)
# print(type(dictA))




# ================================================================================
# Arithmetic Operation

# hasil = 5+2     # penjumlahan
# hasil = 5-2     # pengurangan

# hasil = 5*3     # perkalian
# hasil = 8/2     # pembagian, hasilnya float
# hasil = 8//2    # pembagian, hasilnya integer (dibulatkan ke bawah)
# hasil = 5//2

# hasil = 5**2    # pangkat
# hasil = 5e6     # dikali 10 pangkat sekian

# hasil = 10%4

# print(hasil)



# ================================================================================
# Python function for arithmetic 

# import math

# my_number = 13.4567

# hasil = my_number **2
# hasil = my_number**1/2

# hasil = math.floor(my_number)       # pembulatan ke bawah
# hasil = math.ceil(my_number)        # pembulatan ke atas
# hasil = math.pow(my_number, 2)      # pangkat
# hasil = math.sqrt(my_number)        # akar

# number = -13.45
# hasil = math.fabs(number)           # nilai absolut

# hasil = math.pi

# hasil = round(my_number, 2)         # built-in function

# print(hasil)

# Latinan
# Berapa luas lingkaran yang berdiameter 10 cm?
# Tampilkan dalam pembulatan 3 angka di belakang (.)

# radius = 8/2

# luasLingkaran = math.pi * (radius**2)
# luas = round(luasLingkaran, 3)

# print(luasLingkaran)
# print(luas)




# ================================================================================
# Casting: mengubah data type dari suatu variabel

# myNumber = '123'
# myNumber = '123abc'         # tidak bisa diubah menjadi integer

# print(myNumber)
# print(type(myNumber))

# new_myNumber = int(myNumber)        # casting dari string menjadi integer
# print(new_myNumber)
# print(type(new_myNumber))

# new_myNumber = float(myNumber)        # error, karena sringnya tidak punya angka di belakang point
# print(new_myNumber)
# print(type(new_myNumber))

# myAngka = '123.456'

# new_myAngka = float(myAngka)        # casting dari string menjadi float
# print(new_myAngka)
# print(type(new_myAngka))


# angka = 'abc'

# new_angka = bool(angka)            # casting dari sting menjadi boolean --> True
# print(new_angka)
# print(type(new_angka))


# myNumber = 123

# new_myNumber = str(myNumber)        # casting dari integer menjadi string
# print(new_myNumber)
# print(type(new_myNumber))


# myNumber = 123.456

# new_myNumber = str(myNumber)        # casting dari float menjadi string
# print(new_myNumber)
# print(type(new_myNumber))


# myBool = False

# new_myBool = str(myBool)        # casting dari boolean menjadi string
# print(new_myBool)
# print(type(new_myBool))

# new_myBool = int(myBool)        # casting dari boolean menjadi integer
# print(new_myBool)
# print(type(new_myBool))


# new_myBool = float(myBool)        # casting dari boolean menjadi float
# print(new_myBool)
# print(type(new_myBool))



# ================================================================================
# User input --> meminta input dari user/manusia

# umur = input('Masukkan umur: ')

# print(umur)
# print(type(umur))

# # Buat user input berupa umur, kemudiaan tampilkan umur Anda 5 tahun kemudian
# umur = int(input('Masukkan umur: '))
# umur5TahunLagi = umur + 5

# print(umur5TahunLagi)
# print(type(umur5TahunLagi))



# ================================================================================
# Tanda Petik pada String

# print('saya nonton spiderman')
# # print("saya nonton "spiderman" di bioskop")  # error
# print('saya nonton "spiderman" di bioskop')

# print('''
# saya nonton "spiderman".
# setelah itu saya pulang.
# ''')



# ================================================================================
# Escape character

# print("saya nonton \"spiderman\" di bioskop")  

# print('saya nonton "spiderman".\nsetelah itu saya pulang.')
# print('saya nonton "spiderman".\tsetelah itu saya pulang.')
# print('saya nonton "spiderman".\bsetelah itu saya pulang.')





# ================================================================================
# String function and method

# kata = 'this is python'

# panjangString = len(kata)
# print(panjangString)

# cari_index = kata.index('python')
# print(cari_index)

# splitting = kata.split(' ')
# print(splitting)

# splitting = kata.split('i')
# print(splitting)

# jadiHurufKecil = kata.lower()
# print(jadiHurufKecil)

# jadiHurufBesar = kata.upper()
# print(jadiHurufBesar)

# hurufPertamaCapital = kata.capitalize()
# print(hurufPertamaCapital)



# ================================================================================
# String Slicing/indexing

# kalimat = 'saya belajar python'

# print(kalimat[0])
# print(kalimat[-1])
# print(kalimat[:])
# print(kalimat[:4])
# print(kalimat[0:4])
# print(kalimat[4:])
# print(kalimat[4:-1])
# print(kalimat[4:12])
# print(kalimat[-6:])




# ================================================================================
# String Concatenating

# depan = 'Michael'
# belakang = 'Jordan'

# full_name = depan + belakang
# full_name = depan + ' ' + belakang

# print(full_name)

# print(belakang + str(23))





# ================================================================================
# String Formatting

# umur = 20

# text = 'umur saya' + str(umur) + 'tahun'
# print(text)

# jumlahApel = 3
# jumlahJeruk = 5

# pembelian = 'Saya mau beli apel {} buah dan jeruk {} buah'.format(jumlahApel, jumlahJeruk)
# pembelian = f'Saya mau beli apel {jumlahApel} buah dan jeruk {jumlahJeruk} buah'


# print(pembelian)




# ================================================================================
# String Check 

# kalimat = 'saya sedang belajar python'

# print('bela' in kalimat)
# print('bela' not in kalimat)




# ========================================================================
# String Method (tambahan)

# sentence = 'Saya belajar data science'

# print(sentence.count('a'))
# print(sentence.endswith('ce'))
# print(sentence.isalnum())
# print(sentence.isalpha())
# print(sentence.islower())
# print(sentence.isspace())
# print(sentence.isupper())
# print(sentence.replace('a', 'A'))






















