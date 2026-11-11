# ongkos parkir automater itunger
lama = int(input("Masukkan lama parkir (dalam jam): "))
langganan = input("Apakah Anda pelanggan tetap? (y/n): ").lower()
if langganan == "y":
    tarif = 0
else:
    if lama >= 2:
        tarif = 2000 + (lama - 2) * 1000
    else:
        tarif = 2000
print("Biaya parkir Anda adalah:", tarif)
