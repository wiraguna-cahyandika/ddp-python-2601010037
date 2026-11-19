daftar_belanja = []
while True:
    print("\n=== MENU DAFTAR BELANJA ===")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Lihat Daftar Belanja")
    print("4. Urutkan Daftar Belanja")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "5":
        print("Program selesai.")
        break

    if pilihan == "1":
        barang = input("Masukkan nama barang: ")
        daftar_belanja.append(barang)
        print(f"{barang} telah ditambahkan ke daftar belanja.")
    elif pilihan == "2":
        hapus_barang = input("Masukkan nama barang yang ingin dihapus: ")
        if hapus_barang in daftar_belanja:
            daftar_belanja.remove(hapus_barang)
            print(f"{hapus_barang} telah dihapus dari daftar belanja.")
        else:
            print("Barang tidak ditemukan.")
    elif pilihan == "3":
        if not daftar_belanja:
            print("Daftar belanja kosong.")
        else:
            for index, item in enumerate(daftar_belanja, start=1):
                print(f"{index}. {item}")
    elif pilihan == "4":
        daftar_belanja.sort()
        print("Daftar belanja telah diurutkan.")
    else:
        print("Menu tidak valid!")