jumlah_mhs = int(input("Jumlah mahasiswa: "))
total = 0
jumlah_lulus = 0
nilai_terkecil = float("inf")
nilai_terbesar = float("-inf")

for k in range(1, jumlah_mhs + 1):
    nilai = int(input(f"Nilai mahasiswa ke-{k}: "))
    while nilai < 0 or nilai > 100:
        print("Nilai harus antara 0 dan 100")
        nilai = int(input(f"Nilai mahasiswa ke-{k}: "))
    total += nilai
    nilai_terkecil = min(nilai_terkecil, nilai)
    nilai_terbesar = max(nilai_terbesar, nilai)
    if nilai >= 60:
        jumlah_lulus += 1

rata_rata = total / jumlah_mhs
print(f"Nilai tertinggi: {nilai_terbesar}")
print(f"Nilai terendah: {nilai_terkecil}")
print(f"Rata-rata: {rata_rata:.2f}")
print(f"Lulus: {jumlah_lulus} dari {jumlah_mhs} mahasiswa")
