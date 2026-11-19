def nilai_huruf(nilai):
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"

def is_lulus(nilai):
    return nilai >= 60

## program utama
print(f"nilai_huruf(80) -> {nilai_huruf(80)}")
print(f"is_lulus(80)    -> {is_lulus(80)}")

print(f"nilai_huruf(79) -> {nilai_huruf(79)}")
print(f"is_lulus(79)    -> {is_lulus(79)}")

print(f"nilai_huruf(60) -> {nilai_huruf(60)}")
print(f"is_lulus(60)    -> {is_lulus(60)}")

print(f"nilai_huruf(59) -> {nilai_huruf(59)}")
print(f"is_lulus(59)    -> {is_lulus(59)}")

print(f"nilai_huruf(50) -> {nilai_huruf(50)}")
print(f"is_lulus(50)    -> {is_lulus(50)}")

print(f"nilai_huruf(49) -> {nilai_huruf(49)}")
print(f"is_lulus(49)    -> {is_lulus(49)}")

#latihan12_nilai_huruf.py
#nilai_huruf(80) -> A
#is_lulus(80)    -> True
#nilai_huruf(79) -> B
#is_lulus(79)    -> True
#nilai_huruf(60) -> C
#is_lulus(60)    -> True
#nilai_huruf(59) -> D
#is_lulus(59)    -> False
#nilai_huruf(50) -> D
#is_lulus(50)    -> False
#nilai_huruf(49) -> E
#is_lulus(49)    -> False

# Trace table pembuktian urutan kondisi if-elif:
# Panggilan       | nilai | Kondisi pertama yang True | return
# nilai_huruf(80) | 80    | nilai >= 80               | "A"
# nilai_huruf(79) | 79    | nilai >= 70               | "B"
# nilai_huruf(60) | 60    | nilai >= 60               | "C"
# nilai_huruf(59) | 59    | nilai >= 50               | "D"
# nilai_huruf(50) | 50    | nilai >= 50               | "D"
# nilai_huruf(49) | 49    | else                      | "E"
#
# Analisis jika kondisi nilai >= 60 ditulis sebelum nilai >= 80:
# Jika nilai >= 60 ditaruh paling atas, nilai bagus seperti 80 atau 85 akan
# langsung memenuhi syarat >= 60 (bernilai True), sehingga function langsung
# menjalankan return "C" dan berhenti saat itu juga. Pengecekan untuk grade A
# (>= 80) dan B (>= 70) di bawahnya tidak akan pernah dicek atau dijalankan,
# sehingga nilai tinggi tetap mendapatkan huruf "C".