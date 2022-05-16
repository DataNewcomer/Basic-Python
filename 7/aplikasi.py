# ------------------------------------------------------------------
# Ini formatting string

# for idx, item in enumerate(listBuah):
#     print(idx, '|' ,item['nama'], '\t|' ,item['stok'], '|' ,item['harga'])

# for idx, item in enumerate(listBuah):
#     print('{} | {} \t| {} | {}'.format(idx, item['nama'], item['stok'], item['harga']))

# for idx, item in enumerate(listBuah):
#     print(f"{idx} | {item['nama']} \t| {item['stok']} | {item['harga']}")
# ------------------------------------------------------------------




listBuah = [
    {
        'nama':'Apel',
        'stok':20,
        'harga':10000
    },
    {
        'nama':'Jeruk',
        'stok':15,
        'harga':15000
    },
    {
        'nama':'Anggur',
        'stok':25,
        'harga':20000
    }
]



cart = []

# menampilkan daftar buah
def menampilkanDaftarBuah():
    print('\nDaftar Buah')
    print('Index \t| Nama  \t| Stok\t| Harga')
    for idx, item in enumerate(listBuah):
        print(f"{idx} \t| {item['nama']}  \t| {item['stok']}\t| {item['harga']}")


# menambah buah ke toko
def menambahBuah():
    namaBuah = input('Masukkan nama buah: ')
    stokBuah = input('Masukkan stok buah: ')
    hargaBuah = input('Masukkan harga buah: ')

    listBuah.append({
        'nama':namaBuah,
        'stok':stokBuah,
        'harga':hargaBuah
    })

    menampilkanDaftarBuah() # setelah ditambahkan buahnya, kita mau lihat daftar buahnya lagi

# menghapus buah dari toko
def menghapusBuah():

    menampilkanDaftarBuah() # sebelum menghapus, tampilkan dulu daftar buah apa saja yg tersedia

    indexBuah = int(input('Masukkan index buah yang ingin dihapus: '))
    del listBuah[indexBuah]

    menampilkanDaftarBuah() # tampilkan lagi daftar buah setelah menghapus salah satu item

# membeli buah
def membeliBuah():

    menampilkanDaftarBuah() # sebelum membeli buah, tampilkan dulu daftar buah apa saja yg tersedia

    while True:
        indexBuah = int(input('Masukkan index buah yang ingin dibeli: ')) - 1
        qtyBuah = int(input('Masukkan jumlah yang ingin dibeli: '))
        
        if qtyBuah > listBuah[indexBuah]['stok']:
            print(f"Stok tidak cukup. Stok {listBuah[indexBuah]['nama']} tersisa {listBuah[indexBuah]['stok']} buah")
        else:
            cart.append({
                'nama': listBuah[indexBuah]['nama'],
                'qty': qtyBuah,
                'harga': listBuah[indexBuah]['harga'],
                'index': indexBuah
            })

        print('Isi keranjang belanjaan Anda: ')
        print('Nama  \t| Qty \t| Harga')

        for item in cart:
            print(f"{item['nama']}\t| {item['qty']} \t| {item['harga']}")
        
        checker = input('Mau beli yang lain? [ya/tidak]: ')
        if checker == 'tidak':
            break                   # jika ya, maka akan lanjut looping lagi

    print('Daftar Belanja')
    print('Nama  \t| Qty\t| Harga \t| Total Harga')

    totalHarga = 0
    for item in cart:
        print(f"{item['nama']}\t| {item['qty']}\t| {item['harga']} \t|  {item['qty']*item['harga']}")
        totalHarga = totalHarga + (item['qty'] * item['harga'])

    while True:
        print(f"Total yang harus dibayar: {totalHarga}")

        jumlahUang = int(input('Masukkan jumlah uang Anda: '))
        if jumlahUang > totalHarga:
            kembalian = jumlahUang - totalHarga
            print(f"Terima kasih.\nUang kembalian Anda Rp.{kembalian}")
            for item in cart:
                listBuah[item['index']]['stok'] -= item['qty']
            cart.clear()
            break

        elif jumlahUang == totalHarga:
            print('Terima kasih')
            for item in cart:
                listBuah[item['index']]['stok'] -= item['qty']
            cart.clear()
            break

        else:
            kekurangan = totalHarga - jumlahUang
            print(f"Uang Anda kurang Rp.{kekurangan}")


while True:
    pilihanMenu = input('''
        Selamat Datang di Pasar Buah

        List Menu:
        1. Menampilkan daftar buah
        2. Menambah buah
        3. Menghapus buah
        4. Membeli buah
        5. Exit program

        Silakan pilih nomor menu: ''')

    if pilihanMenu == '1':
        menampilkanDaftarBuah()
    elif pilihanMenu == '2':
        menambahBuah()
    elif pilihanMenu == '3':
        menghapusBuah()
    elif pilihanMenu == '4':
        membeliBuah()
    elif pilihanMenu == '5':
        break                   # keluar dari while loop





