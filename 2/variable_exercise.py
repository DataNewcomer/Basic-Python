# No. 1

# x = 4
# y = 3
# z = 2

# w = ((x+y*z) / (x*y))  ** 2
# print(w)



# ================================================================
# No. 2

# angka = input('Masukkan angka berpapapun: ')    # ini masih string
# hasilKuadrat = int(angka)**2                    # ini tipe datanya integer

# print(f'Kuadrat dari {angka} = {hasilKuadrat}')



# ================================================================
# No. 3

# jumlahHari = int(input('Masukkan jumlah hari: '))     # 485
# print(hari)

# tahun = jumlahHari // 360         # 485//360 = 1
# sisaHari = jumlahHari%360         # 125
# bulan = sisaHari // 30            # 125//30 = 4
# sisaHari = sisaHari%30            # 5
# minggu = sisaHari // 7            # 5 // 7 = 0
# sisaHari = sisaHari%7             # 5
# hari = sisaHari                   # 5

# print(f'{hari} hari terdiri dari {tahun} tahun {bulan} bulan {minggu} minggu {hari} hari')


# ================================================================
# No. 4 

# rasioAndi = 4
# rasioBudi = 10
# totalRasio = rasioAndi + rasioBudi
# totalUmur = 49

# umurAndi = (rasioAndi / totalRasio) * totalUmur
# umurBudi = (rasioBudi / totalRasio) * totalUmur

# print(f'Umur Andi sekarang adalah {umurAndi} tahun')
# print(f'Umur Budi sekarang adalah {umurBudi} tahun')

# print(f'Umur Andi 2 tahun lagi adalah {umurAndi+2} tahun')
# print(f'Umur Budi 2 tahun lagi adalah {umurBudi+2} tahun')


# ================================================================
# No. 5

# jarak = 120             # km
# kecA = 60/3600          # km/detik
# kecB = 40/3600          # km/detik
# start = 9               # satuan jam

# # setiap 3600 detik, mobil akan saling mendekat 100 km
# # setiap 1 detik, mobil mendekat 100/3600

# jarakPerDetik = kecA + kecB
# print(f'Jarak per derik saling mendekat adalah {jarakPerDetik}')

# # untuk terjadi tabrakan, jarak total mendekat harus 120 km

# detikTabrakan = jarak/ jarakPerDetik
# print(f'Tabrakan terjadi setelah {detikTabrakan} detik')

# jam = int(detikTabrakan // 3600)
# sisaDetik = detikTabrakan % 3600

# menit = int(sisaDetik // 60)
# sisaDetik = sisaDetik% 60

# detik = int(sisaDetik)

# print(f'Tabrakan terjadi pada pukul {start+jam}:{menit}:{detik}')


# ================================================================
# No. 6

# jmlApel = int(input('Masukkan jumlah apel: '))
# jmlJeruk = int(input('Masukkan jumlah jeruk: '))
# jmlAnggur = int(input('Masukkan jumlah anggur: '))

# # Diketahui harga buah sebagai berikut:
# hargaApel = 10000
# hargaJeruk = 15000
# hargaAnggur = 20000

# print('Detail Belanja')

# print(f'Apel: \t {jmlApel} x {hargaApel} = {jmlApel*hargaApel}')
# print(f'Jeruk: \t {jmlJeruk} x {hargaJeruk} = {jmlJeruk*hargaJeruk}')
# print(f'Anggur:\t {jmlAnggur} x {hargaAnggur} = {jmlAnggur*hargaAnggur}')

# totalBelanja = (jmlApel*hargaApel) + (jmlJeruk*hargaJeruk) + (jmlAnggur*hargaAnggur)
# print(f'Total belanjaan Anda Rp.{totalBelanja}')



# ================================================================
# # No. 7
# Seorang karyawan memiliki gaji 10 juta rupiah ditahun 2021
# Tahun 2022, gaji naik 25%
# Pajak penghasilan pertahun adalah 12%
# Berapa gaji dia bulan Januari 2022 ini?
# Berapa gaji total 2021 setelah dipotong pajak dalam setahun?
# Berapa gaji total 2022 setelah dipotong pajak dalam setahun?

# gaji2021 = 10000000

# gaji2022 = gaji2021 + ((25/100)*gaji2021)
# gaji_bersih2021 = (gaji2021 - ((12/100)*gaji2021))*12
# gaji_bersih2022 = (gaji2022 - ((12/100)*gaji2022))*12

# print(f'Gaji bulan depan sebesar Rp{gaji2022:,}')
# print(f'Gaji total 2021 setelah dipotong pajak dalam setahun adalah Rp{gaji_bersih2021:,}')
# print(f'Gaji total 2022 setelah dipotong pajak dalam setahun adalah Rp{gaji_bersih2022:,}')




# ================================================================
# No. 8
# # input: masukkan 4 angka: 1234
# # output 3412 (lakukan hanya dengan operasi matematika)

# number = int(input('Masukkan 4 digit angka: ')) # 1234
# a = number/100  # 12.34
# b = number//100 # 12
# c = a-b         # 0.34
# d = c*10000     # 3400
# e = round(d+b)  # 3412
# print(f'Output: {e}')

# # CARA MODULO
# number = int(input('Masukkan 4 digit angka: ')) # 1234
# head = number%100 * 100  # 34*100 = 3400 
# tail = number//100       # 12
# print(head+tail)