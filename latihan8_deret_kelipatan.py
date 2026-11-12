# mesin penhitung kelipatan 5
n = int(input("Masukkan angka: "))
total = 0
deret_teks = ""
for i in range(5, n + 1, 5):
    total += i
    deret_teks += str(i) + " "

print("Kelipatan 5 dari 1 sampai", n, "adalah:", deret_teks)
print("Hasil penjumlahan kelipatan 5 dari 1 sampai", n, "adalah:", total)