# Conditional Statement

# # ===========================================================================
# Boolean: True / False

# print(True)
# print(False)


# # ===========================================================================
# Comparison: operator perbandingan

# print(5>3)      # lebih dari
# print(5>=3)     # lebih dari sama dengan

# print(5<3)      # kurang dari
# print(5<=3)     # kurang dari atau sama dengan

# print(5==3)     # sama dengan
# print(5!=3)     # tidak sama dengan



# # ===========================================================================
# Logical operator: and, or, not

# # and: semuanya True, outputnya True
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
# print()

# # or: minimal ada 1 yang True, outputnya True
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)
# print()

# # not
# print(not True)
# print(not False)




# # ===========================================================================
# Conditional Statement: 
# - program akan melakukan sesuatu tugas, jika suatu kondisi terpenuhi.
# - suatu statement yang melibatkan suatu kondisi untuk menentukan task apa yang akan dikerjakan oleh program, 
#   di mana suatu task tsb hanya akan dikerjakan jika kondisi yang dievaluasi menghasilkan nilai True

# Jika saya haus, maka saya minum
# Jika saya punya uang 20 juta, maka saya membeli iPhone
# Jika belanjaan kamu lebih dari 100 ribu, maka kamu mendapat free ongkir



# # ===========================================================================
# if Statement: 
# - jika kondisi terpenuhi (bernilai True), maka tugas dijalankan oleh program
# - jika kondisi tidak terpenuhi (bernilai False), maka program tidak menjalankan tugas apapun


# if True:                            # ini kondisinya
#     print('Kondisi terpenuhi')      # ini statement/tugas
#     print('Program dijalankan')     # ini statement/tugas

# if umur >= 17:
#     print('Silakan ujian SIM')
#     print('Nanti balik lagi minggu depan ambil SIM nya')



# # ===========================================================================
# if else Statement: 
# - jika kondisi terpenuhi pada if (bernilai True), maka tugas di if statements dijalankan
# - jika kondisi tidak terpenuhi pada if (bernilai False), maka tugas di else statements yang dijalankan

# umur = 16

# if umur >= 17:
#     print('Silakan ujian SIM')
#     print('Nanti balik lagi minggu depan ambil SIM nya')
# else:
#     print('Tunggu sampai Anda 17 tahun')



# # ===================================================================================================
# if elif else Statement: 
# - jika kondisi terpenuhi pada if (bernilai True), maka tugas di if statements dijalankan
# - jika kondisi tidak terpenuhi pada if (bernilai False), maka tugas di elif statements dijalankan
# - jika kondisi tidak terpenuhi pada elif (bernilai False), maka tugas di else statements dijalankan


# nilai = 120

# if (nilai > 90) and (nilai <=100):
#     print('Nilai anda A')
# elif (nilai > 80) and (nilai <=90):
#     print('Nilai anda B')
# elif nilai > 60:
#     print('Nilai anda C')
# else:
#     print('Nilai anda D, anda tidak lulus')




# # =================================================================
# Soal 4

# listA = [True, 13, 'Hello', 2.7] 
# buatlah program untuk mengetahui tipe data dari tiap item dengan menggunakan conditional if
# buat user input berisi index dari listA ('Masukkan index:')
# contoh output:
# - True bertipe data boolean
# - 2.7 bertipe data float


index = 0

