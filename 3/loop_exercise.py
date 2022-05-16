# # ====================================================================================
# # 1. 
# # kalimat = 'Kamu harus menampilkan hanya kata yang berawalan huruf k pada kalimat ini'
# # Tampilkan hanya kata yang berawalan huruf k pada kalimat ini

# kalimat = 'Kamu harus menampilkan hanya kata yang berawalan huruf k pada kalimat ini'

# listKalimat = kalimat.lower().split(' ')
# print(listKalimat)

# for item in listKalimat:
#     if item[0] == 'k':
#         print(item)


# listKalimat = kalimat.split(' ')
# print(listKalimat)

# for item in listKalimat:
#     if (item[0] == 'k') or (item[0] == 'K'):
#         print(item)



# kalimat = 'Kamu harus menampilkan hanya kata yang berawalan huruf k pada kalimat ini'
# listKalimat = kalimat.lower().split(' ')

# for kata in listKalimat:  # ['kamu', 'harus', 'menampilkan', 'hanya', 'kata', 'yang', 'berawalan', 'huruf', 'k', 'pada', 'kalimat', 'ini']
#     for huruf in kata:    # kamu
#         print(huruf)

# makanan = ['nasi','rendang','sambal']

# for sendok in range(1,6):
#     print(f'ini sendok ke {sendok}')

#     for x in makanan:
#         print(f'ambil {x}')
    
        






# # ====================================================================================
# # 2. 
# # Dari angka 1 hingga 50, tampilkan angka yang habis dibagi 3!

# for angka in range(1,51):
#     if angka%3 == 0:
#         print(f'angka {angka} habis jika dibagi 3')
        


# # ====================================================================================
# # 3. 
# # kalimat = 'Tampilkan kata yang memiliki jumlah karakter berjumlah genap pada kalimat ini'
# # Tampilkan kata yang memiliki jumlah karakter berjumlah genap!


# kalimat = 'Tampilkan kata yang memiliki jumlah karakter berjumlah genap pada kalimat ini'

# listKalimat = kalimat.split(' ')

# for kata in listKalimat:
#     if len(kata) % 2 == 0:
#         print(f'kata {kata} \t punya {len(kata)} karakter')



# # ====================================================================================
# # 4. 
# # Buatlah program yang menampilkan integer dari 1 hingga 100 dengan spesifikasi:
#     # - Jika angka merupakan kelipatan 3, maka print 'kelipatan 3'
#     # - Jika angka merupakan kelipatan 5, maka print 'kelipatan 5'
#     # - Jika angka merupakan kelipatan 3 dan 5, maka print 'kelipatan 3 & 5'


# for angka in range(1,101):
#     if (angka%3==0) and (angka%5==0):
#         print(f'{angka} kelipatan 3 & 5')
#     elif angka%3 == 0:
#         print(f'{angka} kelipatan 3')
#     elif angka%5 == 0:
#         print(f'{angka} kelipatan 5')
#     else:
#         print(angka)


# # ====================================================================================

# # 5. 
# # Dari list berikut: [12, 15, 1, 7, 4, 100]
# # Buat algoritma untuk mencari angka tertinggi di dalam list tanpa menggunakan fungsi max atau sort
# # list_angka = [12 ,15, 1, 7, 4, 100]

# listA = [12, 15, 1, 117, 4, 100]

# terbesar = listA[0] 

# for angka in listA:
#     if angka > terbesar:
#         terbesar = angka

# print(f'Angka terbesar dari {listA} adalah {terbesar}')