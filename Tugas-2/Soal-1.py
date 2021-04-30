print("Selamat datang!")
print("--- Menu ---")
print("1. Daftar Kontak")
print("2. Tambah Kontak")
print("3. Keluar")
pelanggan_dict = {
    "nama1" : "Nafi",
    "nomor1" : "08123456789",
    "nama2" : "Joko",
    "nomor2" : "08987654321",
}
pelanggan_list = []

menu = int(input("Pilih menu : "))

while True
if menu == 1 :
    print("Daftar kontak:")
    print("Nama: {}".format(pelanggan_dict["nama1"]))
    print("No telepon: {}".format(pelanggan_dict["nomor1"]))
    print("Nama: {}".format(pelanggan_dict["nama2"]))
    print("No telepon: {}".format(pelanggan_dict["nomor2"]))
elif menu == 2 :
    for i in range(2):
    nama = input("Masukkan Nama anda : ")
    umur = input("Masukkan Nomor anda : ")
    data = {
        "nama3" : nama,
        "nomor3" : umur,
    }
    pelanggan_list.append(data)

for i in pelanggan_list:
    print("Nama Pelanggan : ",i["nama3"])
    print("Nomor Pelanggan : ",i["nomor3"])

data = pelanggan_list[0]
print("Nama pelanggan : ",data["nama3"])
print("Nomors pelanggan : ",data["nomor3"])
elif menu == 3 :
    print("Program selesai, sampai jumpa!")
else:
    print("Menu tidak tersedia")

#masih belum benar kodingannya dan program belum jalan masih susah T_T