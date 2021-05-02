nama_kon = []
no_kon = []
def input_data():
    berapa_data = int(input("Berapa banyak data yang ingin diinput"))
    for i in range(berapa_data):
        print("======================")
        input_nama = str(input("Nama Kontak: "))
        input_telp = input("No. Telp: ")
        print("Kontak Berhasil Ditambahkan")
def tunjuk_kontak():
    for i in range(len(nama_kon)):
        print("Nama: " + nama_kon)
        print("No. Telp: " + no_kon)
print("Selamat Datang!")
while True:
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    print()
    pilihan = int(input("pilihan menu: "))
    if pilihan == 1:
        tunjuk_kontak()
    elif pilihan == 2:
        input_data()
    elif pilihan == 3:
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu Tidak Ditemukan")
        pass