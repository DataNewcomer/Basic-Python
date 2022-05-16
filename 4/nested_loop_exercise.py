# JAWABAN


# ======================================================================================
# No. 1

# Output
# 9 8 7
# 6 5 4
# 3 2 1

# cara 1 ----------------------------------

# for i in range(9,0,-3):           # baris

#     for j in range(i, i-3, -1):   # kolom
#         print(j, end=' ')

#     print()

# cara 2 ----------------------------------

# x = 10
# for i in range(3):                # baris  
#     for j in range(3):            # kolom
#         x -= 1
#         print(x, end = ' ')
#     print()


# ======================================================================================
# No. 2

# * * * * *
# * * * *
# * * *
# * *
# *

# cara 1 ----------------------------------

# for i in range(5,0,-1):       # baris

#     for j in range(i):        # kolom
#         print('*', end=' ')

#     print()


# cara 2 ----------------------------------

# baris = 5

# for i in range(baris + 1, 0, -1): # baris
#     for j in range(0, i - 1):     # kolom
#         print('*', end = ' ')
#     print()





# ======================================================================================
# No. 3

# * * * * *
# * * * *
# * * *
# * *
# *
# * *
# * * *
# * * * *
# * * * * *


# cara 1 ----------------------------------

# for i in range(5,0,-1):

#     for j in range(0, i):
#         print('*', end=' ')

#     print()

# for i in range(1,5,1):

#     for j in range(0, i+1):
#         print('*', end=' ')

#     print()


# cara 2 ----------------------------------

# baris = 5

# for i in range(baris + 1, 1, -1): # baris
#     for j in range(0, i - 1): # kolom
#         print('*', end = ' ')
#     print()

# for i in range(1, baris): # baris
#     for j in range(0, i + 1): # kolom
#         print('*', end = ' ')
#     print()


# cara 3 ----------------------------------

# stars = ''
# size = 5

# for i in range(size) :
#     for j in range(size - i) :
#         stars += '* '
#     stars += '\n'

# for i in range(1, size) :
#     for j in range(i + 1) :
#         stars += '* '
#     stars += '\n'

# print(stars)





# ======================================================================================
# No. 4
# Ketupat

#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *


# cara 1 ----------------------------------

# ketupat = ''
# size = 5

# for i in range(size):                    # ini outer loop

#     for j in range(size - i):            # ini inner loop, akan diselesaikan lebih dahulu
#         ketupat += '  '
#     for k in range(i * 2 + 1):           # ini inner loop, akan diselesaikan lebih dahulu juga
#         ketupat += '* '

#     ketupat += '\n'

# for i in range(1, size):                         # ini outer loop

#     for j in range(i + 1):                       # ini inner loop, akan diselesaikan lebih dahulu
#         ketupat += '  '
#     for k in range((size * 2) - (i * 2) - 1):    # ini inner loop, akan diselesaikan lebih dahulu
#         ketupat += '* '

#     ketupat += '\n'

# print(ketupat)


# cara 2 ----------------------------------

# tinggi = 5

# # segitiga 5 baris atas
# for i in range(1, tinggi*2, 2):             # 1 3 5 7 9
    
#     for j in range((tinggi*2)-1,0,-1):      # 9 8 7 6 5 4 3 2 1
#         if j>i:                             # selama j>i, maka akan mencetak '-'
#             print('-', end='')
#         else:                               # ketika j<=i, maka akan mencetak '0-'
#             print('0-', end='')
#     print()

# # segitiga 4 baris bawah
# for i in range(tinggi*2-3, 0, -2):          # 7 5 3 1

#     for j in range((tinggi*2)-2,-1,-1):     # 8 7 6 5 4 3 2 1 0
#         if j<i:                             # ketika j<i, maka akan mencetak '0-'
#             print('0-', end='')             
#         else:                               # ketika j>=i, maka akan mencetak '-'
#             print('-', end='')  
#     print()



# ======================================================================================
# No. 5
# App Market

# hargaApel = 10000
# hargaJeruk = 15000
# hargaAnggur = 20000

# stockApel = 5
# stockJeruk = 7
# stockAnggur = 6

# while(True) :
#     jumlahApel = int(input('Masukkan Jumlah Apel : '))
#     if(jumlahApel > stockApel) :
#         print('Jumlah yang dimasukkan terlalu banyak \nStock Apel tinggal : ' + str(stockApel))
#     else :
#         break
# while(True) :
#     jumlahJeruk = int(input('Masukkan Jumlah Jeruk : '))
#     if(jumlahJeruk > stockJeruk) :
#         print('Jumlah yang dimasukkan terlalu banyak \nStock Jeruk tinggal : ' + str(stockJeruk))
#     else :
#         break
# while(True) :
#     jumlahAnggur = int(input('Masukkan Jumlah Anggur : '))
#     if(jumlahAnggur > stockAnggur) :
#         print('Jumlah yang dimasukkan terlalu banyak \nStock Anggur tinggal : ' + str(stockAnggur))
#     else :
#         break

# totalHargaApel = jumlahApel * hargaApel
# totalHargaJeruk = jumlahJeruk * hargaJeruk
# totalHargaAnggur = jumlahAnggur * hargaAnggur
# totalHarga = totalHargaAnggur+totalHargaApel+totalHargaJeruk

# print(f'''
#     Detail Belanja

#     Apel : {jumlahApel} x {hargaApel} = Rp.{totalHargaApel:,}
#     Jeruk : {jumlahJeruk} x {hargaJeruk} = Rp.{totalHargaJeruk:,}
#     Anggur : {jumlahAnggur} x {hargaAnggur} = Rp.{totalHargaAnggur:,}

#     Total : Rp.{totalHarga:,}
#     ''')

# while(True) :
#     jmlUang = int(input('Masukkan jumlah uang : '))

#     if(jmlUang > totalHarga) :
#         kembali = jmlUang - totalHarga
#         print(f'Terima kasih \n\nUang kembali anda : Rp.{kembali:,}')
#         break
#     elif(jmlUang == totalHarga) :
#         print('Terima kasih')
#         break
#     else :
#         kekurangan = totalHarga - jmlUang
#         print(f'Uang anda kurang sebesar Rp.{kekurangan:,}')


# :, --> format koma untuk separator ribuan




