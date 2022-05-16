# LATIHAN COLLECTION DATA TYPES

# ====================================================================
# No.1 

# Temukan angka minimum dan maksimum pada list berikut:
# list_angka = [31, 5, 1, 7, 88, 42]
# Output:
# Angka minimum = 1
# Angka maksimum = 88

# # Cara 1 --------------------------------------
list_angka = [31, 5, 1, 7, 88, 42]
# list_angka.sort()

# print(f'angka minimum: {list_angka[0]}')
# print(f'angka maksimum: {list_angka[-1]}')


# # Cara 2 --------------------------------------
# angka_minimum = list_angka[0]
# angka_maksimum = list_angka[0]

# for angka in list_angka: 
#     if(angka < angka_minimum):
#         angka_minimum = angka

#     if(angka > angka_maksimum):
#         angka_maksimum = angka

# print(f'Angka minimum = {angka_minimum}')
# print(f'Angka maksimum = {angka_maksimum}')



# ====================================================================
# No.2

# Urutkan angka pada list berikut dari yang terkecil hingga terbesar tanpa menggunakan method sort!
# list_angka = [31, 5, 1, 7, 88, 42, 202, 29]
# Output
# list_angka_sorted = [1, 5, 7, 29, 31, 42, 88, 202]


# Cara 1 -----------------------------------------------


# list_angka = [31, 5, 1, 7, 88, 42, 202, 29]
# list_angka_sorted = []

# print(f'List angka sebelum diurutkan = {list_angka}')

# for i in range(len(list_angka) - 1):    # range(0,7)

#     for j in range(i+1, len(list_angka)):       # range(1,8)
#         if(list_angka[i] > list_angka[j]):
#             list_angka[i], list_angka[j] = list_angka[j], list_angka[i]
        
# print(f'List angka setelah diurutkan = {list_angka}')



# Jawaban Mba Etha -----------------------------------------------

# list_angka = [31, 5, 1, 7, 88, 42, 202, 29]

# list_baru = []

# while list_angka:
#     min = list_angka[0]
#     for i in list_angka:
#         if i < min:
#             min = i
#     list_baru.append(min)
#     list_angka.remove(min)

# print(list_baru)





# ====================================================================
# No.3

# Buat fungsi untuk mencari berapa kali tiap kata muncul dalam 1 kalimat.
# Contoh:
# kalimat = 'Aku baru makan nasi terus aku mau makan mie nanti malam'
# Output: 
# Jumlah kata 'Aku' ada sebanyak 2
# Jumlah kata 'Baru' ada sebanyak 1
# Jumlah kata 'Makan' ada sebanyak 2
# Jumlah kata 'Terus' ada sebanyak 1
# Jumlah kata 'Mau' ada sebanyak 1
# Jumlah kata 'Mie' ada sebanyak 1
# Jumlah kata 'Nanti' ada sebanyak 1
# Jumlah kata 'Malam' ada sebanyak 1

kalimat = 'Aku baru makan nasi terus aku mau makan mie nanti malam'
kalimat = kalimat.lower().split(' ')
print(kalimat)


# Cara 1 -----------------------------------------------

# kata = {}
    
# for word in kalimat:
#     if word in kata.keys():
#         kata[word] += 1 # Tambahkan 1 value pada key word di dictionary kata
#     else:
#         kata[word] = 1 # Buat key baru dengan value 1 pada dictionary kata
    
# for keys, val in kata.items():
#     print(f'Jumlah kata {keys.capitalize()} ada sebanyak {val}')



# Jawaban Ivan -----------------------------------------------

# kalimat = 'Aku baru makan nasi terus aku mau makan mie nanti malam'
# print(f'''
# Soal 3
# =======
# Kalimat: {kalimat}
# ''')

# kalimat_split = kalimat.lower().split()
# kalimat_filtered = []

# for i in kalimat_split:
#     if i not in kalimat_filtered:
#         kalimat_filtered.append(i)

# for i in range(len(kalimat_filtered)):
#     jumlahKata = kalimat_split.count(kalimat_filtered[i])
#     print(f"Jumlah kata '{str.capitalize(kalimat_filtered[i])}' ada sebanyak {jumlahKata}")    
# print()





# ====================================================================
# No.4 

# Input 5 film, dipisah koma untuk film kesukaan kamu dan kesukaan teman kamu.
# Output: Presentase kesamaan film yang kalian suka
# 'Masukkan 5 film kesukaan Anda dipisahkan dengan tanda koma: '
# 'Masukkan 5 film kesukaan teman Anda dipisahkan dengan tanda koma: '
# 'Kesukaan film kalian yang sama sebesar xx %'

# user1_list = ['spiderman','iron man','the avengers','ant man','thor']
# user2_list = ['spiderman','coco','doraemon','ant man','thor']

# set1 = set(user1_list)
# set2 = set(user2_list)

# kesamaan = set1.intersection(set2)

# jumlah = len(kesamaan)

# if jumlah == 5:
#     print('Kesukaan film kalian yang sama sebesar 100%')
# elif jumlah == 4:
#     print('Kesukaan film kalian yang sama sebesar 80%')
# elif jumlah == 3:
#     print('Kesukaan film kalian yang sama sebesar 60%')
# elif jumlah == 2:
#     print('Kesukaan film kalian yang sama sebesar 40%')
# elif jumlah == 1:
#     print('Kesukaan film kalian yang sama sebesar 20%')    
# else:
#     print('Kalian tidak memiliki kesukaan film yang sama')



# ====================================================================
# No.5 

# # list buah
# listBuah = [
#     ['Apel', 20, 10000],
#     ['Jeruk', 15, 15000],
#     ['Anggur', 25, 20000]
# ]

# # keranjang belanja
# cart = []

# # Jika yang diinput selain angka 1-5, maka akan looping terus meminta inputnya hanya angka 1-5
# while True :

#     # menu utama
#     pilihanMenu = input('''
#         Selamat Datang di Pasar Buah

#         List Menu :
#         1. Menampilkan Daftar Buah
#         2. Menambah Buah
#         3. Menghapus Buah
#         4. Membeli Buah
#         5. Exit Program

#         Masukkan angka Menu yang ingin dijalankan : ''')

#     # Menu 1. menampilkan daftar buah
#     if pilihanMenu == '1':
        
#         # menampilkan daftar buah
#         print('\n Daftar Buah \n')
#         print('Index\t| Nama  \t| Stock\t| Harga')

#         for i in range(len(listBuah)) :
#             print(f'{i}\t| {listBuah[i][0]}  \t| {listBuah[i][1]}\t| {listBuah[i][2]}')

#     # Menu 2. menambah buah
#     elif pilihanMenu == '2':

#         namaBuah = input('Masukkan Nama Buah : ')
#         stockBuah = int(input('Masukkan Stock Buah : '))
#         hargaBuah = int(input('Masukkan Harga Buah : '))

#         # menambah item berupa list pada listBuah menggunakan append()
#         listBuah.append([namaBuah,stockBuah,hargaBuah])
        
#         # menampilkan daftar buah setelah dilakukan penambahan
#         print('\n Daftar Buah \n')
#         print('Index\t| Nama  \t| Stock\t| Harga')
#         for i in range(len(listBuah)) :
#             print(f'{i}\t| {listBuah[i][0]}  \t| {listBuah[i][1]}\t| {listBuah[i][2]}')

#     # Menu 3. menghapus buah
#     elif pilihanMenu == '3':

#         # menampilkan daftar buah setelah dilakukan penambahan
#         print('\n Daftar Buah \n')
#         print('Index\t| Nama  \t| Stock\t| Harga')
#         for i in range(len(listBuah)) :
#             print(f'{i}\t| {listBuah[i][0]}  \t| {listBuah[i][1]}\t| {listBuah[i][2]}')

#         # user input index bari dari buah yang ingin dihapus
#         indexBuah = int(input('Masukkan index buah yang ingin dihapus : '))

#         # menghapus baris pada menu buah
#         del listBuah[indexBuah]

#         # menampilkan daftar buah setelah dilakukan penambahan
#         print('\n Daftar Buah \n')
#         print('Index\t| Nama  \t| Stock\t| Harga')

#         for i in range(len(listBuah)) :
#             print(f'{i}\t| {listBuah[i][0]}  \t| {listBuah[i][1]}\t| {listBuah[i][2]}')

#     # Menu 4. membeli buah
#     elif pilihanMenu == '4':

#         # menampilkan daftar buah setelah dilakukan penambahan
#         print('\n Daftar Buah \n')
#         print('Index\t| Nama  \t| Stock\t| Harga')

#         for i in range(len(listBuah)) :
#             print(f'{i}\t| {listBuah[i][0]}  \t| {listBuah[i][1]}\t| {listBuah[i][2]}')

#         # selama masih mau tambah belanjaan, maka akan dilooping terus 
#         while True :
#             indexBuah = int(input('Masukkan index buah yang ingin dibeli : '))
#             qtyBuah = int(input('Masukkan jumlah yang ingin dibeli : '))
            
#             # jika belanjaan melebihi stok maka tidak masuk keranjang
#             if qtyBuah > listBuah[indexBuah][1]:
#                 print(f'Stock tidak cukup, stock {listBuah[indexBuah][0]} tinggal {listBuah[indexBuah][1]}')

#             # jika jumlah belanajaan masih tersedia  
#             else :
#                 cart.append([listBuah[indexBuah][0], qtyBuah, listBuah[indexBuah][2], indexBuah])
            
#             # tampilan isi keranjang belanjaan
#             print('Isi Cart :')
#             print('Nama\t| Qty\t| Harga')
#             for item in cart :
#                 print(f'{item[0]}\t| {item[1]}\t| {item[2]}')
            
#             # cek apakah mau tambah belanjaan
#             checker = input('Mau beli yang lain? (ya/tidak) = ')
            
#             # kalau 'ya' maka akan looping terus, kalau tidak ada lagi yang mau dibeli maka keluar dari sistem looping keanjang belanja
#             if(checker == 'tidak') :
#                 break

#         # menampilkan daftar belanja
#         print('Daftar Belanja :')
#         print('Nama\t| Qty\t| Harga\t| Total Harga')
        
#         totalHarga = 0
#         for item in cart :
#             print(f'{item[0]}\t| {item[1]}\t| {item[2]}\t| {item[1] * item[2]}')
#             totalHarga += item[1] * item[2]    
        
#         # kalau uangnya kurang, akan dilooping terus
#         while True :
#             print(f'Total Yang Harus Dibayar = {totalHarga}')
#             jmlUang = int(input('Masukkan jumlah uang : '))
        
#             # uang yang dibayar lebih dari total harga
#             if(jmlUang > totalHarga) :
#                 kembali = jmlUang - totalHarga
#                 print(f'Terima kasih \n\nUang kembali anda : {kembali}')
        
#                 for item in cart :
#                     listBuah[item[3]][1] -= item[1]
#                 cart.clear()
#                 break
        
#             # uang yang dibayar pas
#             elif(jmlUang == totalHarga) :
#                 print('Terima kasih')
        
#                 for item in cart :
#                     listBuah[item[3]][1] -= item[1]
#                 cart.clear()
#                 break

#             # uang kurang, maka nanti akan dilooping sampai bayar uangnya pas atau lebih
#             else :
#                 kekurangan = totalHarga - jmlUang
#                 print(f'Uang anda kurang sebesar {kekurangan}')

#     # looping menu utama selesai, exit dari aplikasi
#     elif pilihanMenu == '5':
#         break
    




# ====================================================================
# No.6


# # list buah
# listBuah = [
#     {
#         'nama': 'Apel',
#         'stock': 20,
#         'harga': 10000
#     },
#     {
#         'nama': 'Jeruk',
#         'stock': 15,
#         'harga': 15000
#     },
#     {
#         'nama': 'Anggur',
#         'stock': 25,
#         'harga': 20000
#     }
# ]

# # keranjang belanja
# cart = []

# # Jika yang diinput selain angka 1-5, maka akan looping terus meminta inputnya hanya angka 1-5
# while True :

#     # menu utama akan selalu ditampilkan lagi setelah selesai proses menu 1/2/3/4 karena while masih True
#     pilihanMenu = input('''
#         Selamat Datang di Pasar Buah

#         List Menu :
#         1. Menampilkan Daftar Buah
#         2. Menambah Buah
#         3. Menghapus Buah
#         4. Membeli Buah
#         5. Exit Program

#         Masukkan angka Menu yang ingin dijalankan : ''')

#     # Menu 1. menampilkan daftar buah
#     if pilihanMenu == '1':
        
#         # menampilkan daftar buah
#         print('\n Daftar Buah \n')
#         print('Index\t| Nama  \t| Stock\t| Harga')

#         for i in range(len(listBuah)) :
#             print(f'{i}\t| {listBuah[i]["nama"]}  \t| {listBuah[i]["stock"]}\t| {listBuah[i]["harga"]}')

#     # Menu 2. menambah buah
#     elif pilihanMenu == '2':

#         namaBuah = input('Masukkan Nama Buah : ')
#         stockBuah = int(input('Masukkan Stock Buah : '))
#         hargaBuah = int(input('Masukkan Harga Buah : '))

#         # menambah item berupa DICTIONARY pada listBuah menggunakan append()
#         listBuah.append({"nama":namaBuah,
#                          "stock":stockBuah,
#                          "harga":hargaBuah
#                          })
        
#         # menampilkan daftar buah setelah dilakukan penambahan
#         print('\n Daftar Buah \n')
#         print('Index\t| Nama  \t| Stock\t| Harga')
#         for i in range(len(listBuah)) :
#             print(f'{i}\t| {listBuah[i]["nama"]}  \t| {listBuah[i]["stock"]}\t| {listBuah[i]["harga"]}')

#     # Menu 3. menghapus buah
#     elif pilihanMenu == '3':

#         # menampilkan daftar buah setelah dilakukan penambahan
#         print('\n Daftar Buah \n')
#         print('Index\t| Nama  \t| Stock\t| Harga')
#         for i in range(len(listBuah)) :
#             print(f'{i}\t| {listBuah[i]["nama"]}  \t| {listBuah[i]["stock"]}\t| {listBuah[i]["harga"]}')

#         # user input index bari dari buah yang ingin dihapus
#         indexBuah = int(input('Masukkan index buah yang ingin dihapus : '))

#         # menghapus baris pada menu buah
#         del listBuah[indexBuah]

#         # menampilkan daftar buah setelah dilakukan penambahan
#         print('\n Daftar Buah \n')
#         print('Index\t| Nama  \t| Stock\t| Harga')

#         for i in range(len(listBuah)) :
#             print(f'{i}\t| {listBuah[i]["nama"]}  \t| {listBuah[i]["stock"]}\t| {listBuah[i]["harga"]}')

#     # Menu 4. membeli buah
#     elif pilihanMenu == '4':

#         # menampilkan daftar buah setelah dilakukan penambahan
#         print('\n Daftar Buah \n')
#         print('Index\t| Nama  \t| Stock\t| Harga')

#         for i in range(len(listBuah)) :
#             print(f'{i}\t| {listBuah[i]["nama"]}  \t| {listBuah[i]["stock"]}\t| {listBuah[i]["harga"]}')

#         # selama masih mau tambah belanjaan, maka akan dilooping terus 
#         while True :
#             indexBuah = int(input('Masukkan index buah yang ingin dibeli : '))
#             qtyBuah = int(input('Masukkan jumlah yang ingin dibeli : '))
            
#             # jika belanjaan melebihi stok maka tidak masuk keranjang
#             if qtyBuah > listBuah[indexBuah]["stock"]:
#                 print(f'Stock tidak cukup, stock {listBuah[indexBuah]["nama"]} tinggal {listBuah[indexBuah]["stock"]}')

#             # jika jumlah belanajaan masih tersedia (DICTIONARY)
#             else :
#                 cart.append({'nama':listBuah[indexBuah]["nama"], 
#                              'qty':qtyBuah,
#                              'harga':listBuah[indexBuah]["harga"], 
#                              'index':indexBuah
#                              })
            
#             # tampilan isi keranjang belanjaan
#             print('Isi Cart :')
#             print('Nama\t| Qty\t| Harga')
#             for item in cart :
#                 print(f'{item["nama"]}\t| {item["qty"]}\t| {item["harga"]}')
            
#             # cek apakah mau tambah belanjaan
#             checker = input('Mau beli yang lain? (ya/tidak) = ')
            
#             # kalau 'ya' maka akan looping terus, kalau tidak ada lagi yang mau dibeli maka keluar dari sistem looping keanjang belanja
#             if(checker == 'tidak') :
#                 break

#         # menampilkan daftar belanja
#         print('Daftar Belanja :')
#         print('Nama\t| Qty\t| Harga\t| Total Harga')
        
#         totalHarga = 0
#         for item in cart :
#             print(f'{item["nama"]}\t| {item["qty"]}\t| {item["harga"]}\t| {item["qty"] * item["harga"]}')
#             totalHarga += item["qty"] * item["harga"]    
        
#         # kalau uangnya kurang, akan dilooping terus
#         while True :
#             print(f'Total Yang Harus Dibayar = {totalHarga}')
#             jmlUang = int(input('Masukkan jumlah uang : '))
        
#             # uang yang dibayar lebih dari total harga
#             if(jmlUang > totalHarga) :
#                 kembali = jmlUang - totalHarga
#                 print(f'Terima kasih \n\nUang kembali anda : {kembali}')
        
#                 for item in cart :
#                     listBuah[item["index"]]["stock"] -= item["qty"]
#                 cart.clear()
#                 break
        
#             # uang yang dibayar pas
#             elif(jmlUang == totalHarga) :
#                 print('Terima kasih')
        
#                 for item in cart :
#                     listBuah[item["index"]]["stock"] -= item["qty"]
#                 cart.clear()
#                 break

#             # uang kurang, maka nanti akan dilooping sampai bayar uangnya pas atau lebih
#             else :
#                 kekurangan = totalHarga - jmlUang
#                 print(f'Uang anda kurang sebesar {kekurangan}')

#     # looping menu utama selesai, exit dari aplikasi
#     elif pilihanMenu == '5':
#         break