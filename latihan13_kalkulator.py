def tambah(a, b):
    return a + b
def kurang(a, b):
    return a - b
def kali(a, b):
    return a * b
def bagi(a, b):
    if b == 0:
        return None
    return a / b

while True:
    print("\n=== MENU KALKULATOR ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "5":
        print("Program selesai.")
        break

    if pilihan in ("1", "2", "3", "4"):
        a = float(input("Masukkan angka pertama (a): "))
        b = float(input("Masukkan angka kedua (b): "))

        if pilihan == "1":
            print("Hasil:", tambah(a, b))
        if pilihan == "2":
            print("Hasil:", kurang(a, b))
        if pilihan == "3":
            print("Hasil:", kali(a, b))
        if pilihan == "4":
            hasil = bagi(a, b)
            if hasil is None:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
            else:
                print("Hasil:", hasil)
    else:
        print("Menu tidak valid!")