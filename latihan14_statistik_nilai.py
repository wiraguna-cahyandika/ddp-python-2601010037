jml_mhs = int(input("Masukkan jumlah mahasiswa: "))
nilai = []
for i in range(jml_mhs):
    n = int(input(f"Masukkan nilai mahasiswa ke-{i+1}: "))
    nilai.append(n)
rata_rata = sum(nilai) / jml_mhs
di_atas = 0
for n in nilai:
    if n > rata_rata:
        di_atas += 1
print(nilai)
print(f"Tertinggi: {max(nilai)}")
print(f"Terendah: {min(nilai)}")
print(f"Rata-rata nilai: {rata_rata:.2f}")
print(f"Di atas rata-rata: {di_atas}")