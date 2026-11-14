# tebak angka
angka_rahasia = 31
tebakan = int(input("Tebak angka antara 1 sampai 50: "))
jumlah_tebakan = 1
while tebakan != angka_rahasia:
    if tebakan > angka_rahasia:
        print("terlalu besar.")
    else:
        print("terlalu kecil.")
    tebakan = int(input("Coba lagi: "))
    jumlah_tebakan += 1
print(f"Benar! {jumlah_tebakan} kali tebakan.")