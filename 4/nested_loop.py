# BREAK, CONTINUE, PASS (Loop Control Statements)
# Kita dapat menggunakan break, continue, dan pass statements dalam loop 
# untuk menambah fungsional tambahan dalam berbagai macam kasus

# break     ---> kelaur dari sistem looping
# continue  ---> melewati suatu tugas pada looping, lalu melanjutkan ke putaran selanjunya
# pass      ---> tidak melakukan apa-apa

# ============================================================================
# break

# kalimat = 'membuka sepatu'

# for item in kalimat:
#     if item == 'a':
#         break         # keluar dari sistem looping
#     print(item)


# ============================================================================
# continue

# kalimat = 'membuka sepatu'

# for item in kalimat:
    
#     if item == 'a':
#         continue        # tidak melakukan tugas setelah statement cotinue, langsung lanjut ke putaran berikutnya
    
#     print(item)

# ============================================================================
# pass

# kalimat = 'membuka sepatu'

# for item in kalimat:
#     pass                # agar tidak error jika belum tau statement apa yang ingin ditulis pada looping

# print('Hello world')



# ============================================================================
# Contoh lain: break vs continue

# break
# x = 0 

# while x<10:

#     x = x+1
#     print(f'ini adalah angaka {x}')

#     if x == 3:
#         print('HORE ANGKA 3 KETEMU')
#         break


#     print('angka masih kurang dari 10')
#     print('lanjut ke angka selanjutnya')



# continue
# x = 0 

# while x<10:

#     x = x+1
#     print(f'ini adalah angaka {x}')
    
#     if x == 3:
#         print('HORE ANGKA 3 KETEMU')
#         print()
#         # continue


#     print('angka masih kurang dari atau sama dengan 10')
#     print('lanjut ke angka selanjutnya')
#     print()




# ============================================================================
# NESTED LOOP
# looping di dalam looping
# inner looping akan diselesaikan dulu, kalau sudah selesai, kemudian lanjut ke outer looping

# Contoh 1 
# for loop di dalam for loop

# sendok = range(5)   # 0 1 2 3 4
# piring = ['nasi','rendang','sayur','sambal']

# for i in sendok:
#     print(f'ini sendok ke {i+1}')

#     for j in piring:
#         print(j)


# # Contoh lain
# sendok = range(5)   # 0 1 2 3 4
# piring = ['nasi','rendang','sayur','sambal']

# for i in sendok:
#     print(f'ini sendok ke {i+1}')

#     # for j in piring:
#     #     if (j == piring[0]) or (j == piring[1]):
#     #         print(j)

#     for j in piring:
#         if j in piring[0:2]:
#             print(j)



# Contoh 2
# for loop di dalam while loop

# sendok = range(5)   # 0 1 2 3 4
# piring = ['nasi','rendang','sayur','sambal']

# i = 0

# while i < 5:
#     print(f'ini sendok ke {i+1}')

#     for j in piring:
#         print(j)

#     i = i+1
    


# Latihan 1

# Output:
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1


# for i in range(3):                  # ---> ini outer looping 0 1 2

#     for j in range(5):              # ---> ini inner looping 0 1 2 3 4 
#         print(1, end=' ')

#     print()



# Latihan 2

# Output:
# 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5

# for i in range(3):                  # ---> ini outer looping

#     for j in range(1,6):              # ---> ini inner looping
#         print(j, end=' ')




# ============================================================================
# LOOP DRAWING
# Menggambar pola dengan kode python

# Contoh 1
# Menggambar persegi panjang
# panjang hor = 3 baris
# lebar ver = 5 kolom

# kolom = 4
# baris = 4

# for i in range(baris):

#     for j in range(kolom):
#         print('*', end=' ')

#     print()


# Contoh 2
# Menggambar segitiga samakaki

# *
# * *
# * * *
# * * * *

# kaki = 4

# for i in range(1, kaki+1):           # 1 2 3 4

#     for j in range(1, i+1):          # range(1,3) --> 1 2
#         print('*', end=' ')

#     print()

