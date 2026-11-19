def cari_nilai(data, x):
    for i in range(len(data)):
        if data[i] == x:
            return i
    return -1
def balik(data):
    hasil = []
    for i in range(len(data) - 1, -1, -1):
        hasil.append(data[i])
    return hasil
print(cari_nilai([5, 8, 2], 8))
print(cari_nilai([5, 8, 2], 7))
print(balik([5, 8, 2]))

# Trace Table: cari_nilai([5, 8, 2], 7)
# ---------------------------------------------------------
# Putaran | i | data[i] | data[i] == 7 | Keterangan
# ---------------------------------------------------------
#    1    | 0 |    5    |    False     | Lanjut ke i berikutnya
#    2    | 1 |    8    |    False     | Lanjut ke i berikutnya
#    3    | 2 |    2    |    False     | Loop selesai
# ---------------------------------------------------------
# Setelah loop selesai: menjalankan return -1 (hasil: -1)