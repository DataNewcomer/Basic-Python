
# COLLECTION DATA TYPES

# ====================================================================================
# LIST
# ====================================================================================

# - Dapat menampung berbagai macam tipe data (string, integer, boolean, dll) secara bersamaan
# - Dapat menampung nilai nilai yang sama atau duplikat
# - Mutable, item dalam list bisa diubah/diganti
# - Berurutan, jadi bisa di-indexing
# - Ditandai dengan []

# list_contoh1 = ['Hello', 1, 10, 100, True]           # list bisa menampung berbagai macam tipe data
# print(list_contoh1)

# listDalamList = ['python', 'jakarta', [5,6,7]]      # list bisa menampung list
# print(listDalamList)

# list_contoh2 = ['Hello', 1, 10, 100, True, 6, 6, 6]  # item dalam list boleh duplikat
# print(list_contoh2)

# print(list_contoh2[4])

# list_contoh2[4] = False                             # item dalam list bisa diganti (mutable)

# print(list_contoh2)
# print(list_contoh2[4])




# ===================================================================
# Indexing pada list

# list_contoh2 = ['Hello', 1, 10, 100, True, 6, 6, 6]  
# index ---->       0      1   2   3    4    5  6  7 
# index ---->      -8     -7  -6  -5   -4   -3 -2 -1 

# list_contoh = ['Hello', 1, 10, 100, True, 6, 6, 6]

# print(list_contoh[0])
# print(list_contoh[1])
# print(list_contoh[2])
# print(list_contoh[3])
# print(list_contoh[4])
# print(list_contoh[5])
# print(list_contoh[6])
# print(list_contoh[7])




# ===================================================================
# Slicing pada list

# list_contoh = ['Hello', 1, 10, 100, True, 6, 6, 6]

# print(list_contoh[-3:])         # [6, 6, 6]
# print(list_contoh[2:4])         # [10, 100]
# print(list_contoh[0:7])         # ['Hello', 1, 10, 100, True, 6, 6]
# print(list_contoh[0:-1])        # ['Hello', 1, 10, 100, True, 6, 6]
# print(list_contoh[:])           # ['Hello', 1, 10, 100, True, 6, 6, 6]




# ===================================================================
# Cek keberadaan suatu item pada list

# list_contoh = ['Hello', 1, 10, 100, True, 6, 6, 6]

# if 9 in list_contoh:
#     print('Ditemukan') 
# else:
#     print('Tidak ditemukan')




# ===================================================================
# Berapa jumlah item pada list

# list_contoh = ['Hello', 1, 10, 100, True, 6, 6, 6]
# (len(list_contoh))         # berisi 8 item/element




# ===================================================================
# Copy list

# list_contoh = ['Hello', 1, 10, 100, True, 6, 6, 6]
# # print(list_contoh)

# list_baru = list_contoh                         # hati-hati! apa yg diubah pada list_baru akan terunah juga di list_contoh 

# print('ini list_baru', list_baru)
# print('ini list_contoh', list_contoh)

# list_baru[4] = False                

# print('ini list_baru', list_baru)               # list_baru index 4 True berubah jadi False
# print('ini list_contoh', list_contoh)           # list_contoh index 4 True ikut-ikutan berubah jadi False

# print()

# -------------------------------------------------

# list_contoh = ['Hello', 1, 10, 100, True, 6, 6, 6]
# # print(list_contoh)

# list_baru = list_contoh.copy()

# print('ini list_baru', list_baru)
# print('ini list_contoh', list_contoh)

# list_baru[4] = False

# print('ini list_baru', list_baru)               # list_baru index 4 True berubah jadi False
# print('ini list_contoh', list_contoh)           # list_contoh index 4 True tetap True




# ===================================================================
# List Concatenating

# list_angka = [1,2,3,4,5]
# list_huruf = ['a','b','c']

# list_concate = list_angka + list_huruf        # list_angka duluan
# print(list_concate)

# list_concate = list_huruf + list_angka        # list_huruf duluan
# print(list_concate)




# ===================================================================
# Mecari index suatu item pada list

# list_contoh = ['Hello', 1, 10, 100, True, 6, 6, 6]
# print(list_contoh.index(100))




# ===================================================================
# Sorting/mengurutkan item dalam list

# mobil = ['toyota', 'ferrari', 'bmw', 'mercedes', 'hyundai'] 

# mobil.sort()        # sorting ascending
# print(mobil)

# mobil.reverse()     # sorting descending
# print(mobil)


# alphanum = ['b', 'z', 1, 'a', 999, 'A', 'Z', 'B', 50 ]   # error, tidak bisa membandingkan integer dengan string

# alphanum.sort()
# print(alphanum)


# alphabet = ['b', 'z', 'a', 'A', 'Z', 'B']   # prioritas huruf capital duluan

# alphabet.sort()
# print(alphabet)




# ===================================================================
# List 2 dimensi

# kendaraan = [['mobil','ferrari'], 
#              ['motor','ducati']]

# print(kendaraan)

# vehicle = ['mobil', 'ferrari', 'motor', 'ducati']
# print(vehicle)

# print(vehicle[1])

# print(kendaraan[1][1])




# ===================================================================
# List 3 dimensi

# list_bilangan = [[[1,  2,  3], 
#                   [100,200,300]],

#                  [[4,  5,  6], 
#                   [400,500,600]]]

# print(list_bilangan[1][0][2])




# ===================================================================
# metod/function .append() --> menambahkan item di index terakhir

# mobil = ['toyota', 'ferrari', 'bmw', 'mercedes', 'hyundai'] 
# mobil_baru = ['honda', 'vw']

# mobil = mobil + mobil_baru          # concatenating
# print(mobil)
# print(len(mobil))

# mobil.append(mobil_baru)            # append
# print(mobil)
# print(len(mobil))

# mobil.append('lamborghini')
# print(mobil)




# ===================================================================
# Menyelipkan item pada list

# mobil = ['toyota', 'ferrari', 'bmw', 'mercedes', 'hyundai'] 
# print(mobil)

# mobil.insert(1, 'suzuki')
# print(mobil)




# ===================================================================
# Menghapus item pada list

# mobil = ['toyota', 'ferrari', 'bmw', 'mercedes', 'hyundai'] 
# print(mobil)

# mobil.remove('bmw')     # menghapus 'bmw' pertama
# print(mobil)

# mobil.pop()             # menghapus item terakhir
# print(mobil)

# del mobil[1]            # menghapus item pada index 1
# print(mobil)

# mobil.clear()           # menghapus seluruh item dalam list
# print(mobil)




# ===================================================================
# List Comprehension --> membuat sebuah list yang basis logikanya berasala dari for loop


# Buatlah list berisi angka genap dimulai dari 2-10
# list_genap = []

# for i in range(2,11,2):     # 2 4 6 8 10
#     list_genap.append(i)

# print(list_genap)


# Buatlah list berisi [1,10,100,1000] 10**0 10**1 10**2 10**3
# list10pangkat = []

# for i in range(0,4):
#     list10pangkat.append(10**i)

# print(list10pangkat)


# Buatlah list berisi [1,4,9,16] 

# list_kuadrat = []

# for i in range(1,5):
#     list_kuadrat.append(i**2)

# print(list_kuadrat)


# list_kuadrat = [i**2 for i in range(1,5)]
# print(list_kuadrat)

# list10pangkat = [10**i for i in range(0,4)]
# print(list10pangkat)





# ===============================================================================
# TUPLE
# ====================================================================================


# - Mirip dengan list, dapat menyimpan banyak item dengan berbagai macam tipe data
# - Immutable, item dalam tuple tidak dapat diubah/diganti
# - Berurutan, jadi bisa di-indexing
# - Ditandai dengan ()

# tuple_contoh = ('Hello', 1, 10, 100, True, 6, 6, 6)
# print(tuple_contoh)

# print(tuple_contoh[3])      # tuple bisa diindexing, karena punya urutan

# tuple_contoh[3] = 9         # immutable, item dalam tuple tidak bisa diganti
# print(tuple_contoh)


# # Jika tetap mau ganti item dalam tuple, harus diubah ke list dulu, kemudian diubah lagi ke tuple
# listA = list(tuple_contoh)
# print(listA)

# listA[3] = 9
# print(listA)

# tuple_contoh = tuple(listA)
# print(tuple_contoh)




# ===============================================================================
# Jika ingin buat tuple berisi 1 item, tambahkan koma di belakangnya
# tuple_mobil = ('toyota',)
# print(tuple_mobil)
# print(len(tuple_mobil))

# list_mobil = ['toyota']
# print(list_mobil)



# ===============================================================================
# cara cek item dalam tuple mirip dengan cek item dalam list
# cara concatenate pada tuple mirip dengan concatenate pada list
# cara tau jumlah item pada tuple mirip dengan cara tau jumlah item pada list
# tuple 2 dimensi mirip dengan list 2 dimensi




# ===============================================================================
# DICTIONARY
# ===============================================================================

# Kontainer yang bisa menampung banyak value dengan beragam tipe data
# Tidak punya urutan, tidak bisa indexing pakai angka
# Indexing dengan key-nya
# dictionary terdiri dari {key:value} 
# key adalah kata kuncinya, tidak bleh duplikat
# dictionary digunakan ketika data tersebut memiliki pola, atau tipe data yang sama tetapi berhubungan satu dengan yang lain

# dict_contoh = {'nama':'Andi', 'umur':20, 'domisili':'jakarta'}
# print(dict_contoh)

# print(dict_contoh['umur'])              # indexing dengan key


# dict_contoh['domisili'] = 'bandung'     # dictionary mutable, valuenya bisa diganti
# print(dict_contoh)

# dict_contoh['gender'] = 'male'          # bisa menambahkan item
# print(dict_contoh)


# ===============================================================================
# Cara lain membuat dictionary

# dictB = dict(nama='Andi', umur=20, domisili='bogor')
# print(dictB)




# ===============================================================================
# Cara mengakses value dalam dictionary

# dictB = dict(nama='Andi', umur=20, domisili='bogor')
# print(dictB.get('nama'))




# ===============================================================================
# Menghapus item pada dictionary

# dict_contoh = {'nama':'Andi', 'umur':20, 'domisili':'jakarta'}
# print(dict_contoh)          # sebelum dihapus
# del dict_contoh['umur']     # menggunakan del
# print(dict_contoh)          # sesudah dihapus

# dict_contoh = {'nama':'Andi', 'umur':20, 'domisili':'jakarta'}
# print(dict_contoh)            # sebelum dihapus
# dict_contoh.pop('domisili')   # menghapus dengan pop
# print(dict_contoh)            # setelah dihapus


# dict_contoh = {'nama':'Andi', 'umur':20, 'domisili':'jakarta'}
# print(dict_contoh)      # sebelum dihapus
# dict_contoh.popitem()   # menghapus item terakhir
# print(dict_contoh)      # sesudah dihapus



# ===============================================================================
# Looping pada dictionary

# dict_contoh = {'nama':'Andi', 'umur':20, 'domisili':'jakarta'}

# for i in dict_contoh:
#     print(i)

# for i in dict_contoh.keys():
#     print(i)

# for i in dict_contoh.values():
#     print(i)

# for k, v in dict_contoh.items():
#     print(k)
#     print(v)



# ===============================================================================
# Cara copy dictionary

# dict_contoh = {'nama':'Andi', 'umur':20, 'domisili':'jakarta'}

# dict_baru = dict_contoh.copy()
# print(dict_baru)

# dict_baru['umur'] = 23
# print(dict_baru)

# print(dict_contoh)



# ===============================================================================
# Nested Dictionary

# makanan = {
#     'pembuka':{'nama':'sup', 'harga':30000},
#     'main_course':{'nama':'nasgor', 'harga':50000},
#     'penutup':{'nama':'puding', 'harga':20000}
# }
# print(makanan)


# print(makanan['penutup']['harga'])      # indexing pada nested dictionary dengan key-nya
# print(makanan['main_course']['nama'])




# ===============================================================================
# Membuat dictionary dari list

# list_siswa = [['Andi',23,'Jakarta'], ['Budi',30,'Medan'], ['Caca',19,'Bandung']]

# dict_siswa = {}

# for i in list_siswa:        # ['Andi',23,'Jakarta']
#     key = i[0]
#     val = i[1:3]

#     dict_siswa[key] = val

# print(dict_siswa)





# ===============================================================================
# SET
# ===============================================================================

# - Dapat menyimpan banyak item dengan berbagai macam tipe data
# - Tidak bisa duplikat, semua item unique 
# - Tidak punya urutan, jadi tidak bisa diindexing
# - Set bisa digunakan untuk memfilter duplikat
# - Ditandai dengan {}

# set_contoh = {1,2,3,4,5,2,2,5}      # tidak bisa duplikat
# print(set_contoh)

# set_contoh = {1,2,3,4,5,2,2,5} 
# print(set_contoh[0])                # tidak bisa diindexing

# set_contoh = {1,2,3,4,5,2,2,5} 

# for i in set_contoh:
#     print(i)


# set_examp = {'toyota','honda','suzuki','ferrari','honda'}       # tidak punya urutan, tapi bisa dilooping
# for i in set_examp:
#     print(i)


# ===============================================================================
# Membuat set dari list, tuple, dictionary

# list_mobil = ['toyota','honda','suzuki','ferrari','honda']
# print(set(list_mobil))

# tuple_mobil = ('toyota','honda','suzuki','ferrari','honda')
# print(set(tuple_mobil))

# dict_siswa = {'nama':'Andi', 'umur':20, 'domisili':'jakarta'}
# print(set(dict_siswa))

# dict_siswa = {'nama':'Andi', 'umur':20, 'domisili':'jakarta'}
# print(set(dict_siswa.values()))


# ===============================================================================
# cek keberadaan item pada set mirip dengan cek keberadaan item pada list



# ===============================================================================
# Menambahkan item pada set
# set_examp = {'toyota','honda','suzuki','ferrari','honda'}       

# set_examp.add('bmw')
# print(set_examp)

# set_examp.add('toyota')     # tidak mau menambahkan item, karena tidak boleh duplikat
# print(set_examp)

# set_examp.update('mercedes')     
# print(set_examp)

# set_examp.update({'mercedes','bentley'})   # update() bisa digunakan untuk menambahkan >1 item pada set   
# print(set_examp)



# ===============================================================================
# Menghapus item pada set

# set_examp = {'toyota','honda','suzuki','ferrari','honda'}     

# set_examp.remove('suzuki')
# print(set_examp)

# set_examp.discard('ferrari')
# print(set_examp)

# set_examp.pop()           # menghapus item secara acak
# print(set_examp)

# set_examp.clear()           # menghapus semua item dalam set
# print(set_examp)




# ===============================================================================
# Union, Difference, Symmetric Difference, Intersection

# ganjil = {1,3,5,7,9}
# prima = {2,3,5,7,11}

# set_union = ganjil.union(prima)                 # full outer join
# print(set_union)

# set_difference = ganjil.difference(prima)       # yang ada di ganjil, tidak ada di prima
# print(set_difference)

# # ganjil.difference_update(prima)                 # mengupdate item dari ganjil, dimana item-item tsb tidak ada di prima
# # print(ganjil)

# set_sym_difference = ganjil.symmetric_difference(prima)   # hanya dimiliki oleh ganjil dan hanya dimiliki oleh prima    
# print(set_sym_difference)

# set_intersection = ganjil.intersection(prima)      # sama-sama dimiliki oleh ganjil dan prima
# print(set_intersection)




# ===============================================================================
# Cek subset, superset, disjoint

# ganjil = {1,3,5,7,9}
# angka = {3,5}

# print(angka.issubset(ganjil))       # apakah angka adalah subset dari ganjil
# print(angka.issuperset(ganjil))
# print(ganjil.issuperset(angka))     # apakah ganjil adalah superset dari angka
# print(angka.isdisjoint(ganjil))     # apakah kedua set benar benar itemnya berbeda




# ===============================================================================
# ZIP

angka = [1,2,3]
huruf = ['a','b','c']

print(zip(angka, huruf))

print(list(zip(angka, huruf)))


for i in zip(angka,huruf):
    print(i)
