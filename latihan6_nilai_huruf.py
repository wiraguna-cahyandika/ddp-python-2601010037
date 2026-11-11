# nilai lulus enggak
nilai = int(input("Masukkan nilai: "))
if nilai >= 0 and nilai <= 100:
    if nilai >= 80:
        nilai = "A"
    elif nilai >= 70:
        nilai = "B"
    elif nilai >= 60:
        nilai = "C"
    else:
        nilai = "D"
    if nilai == "A" or nilai == "B" or nilai == "C":
        print("Selamat, Anda lulus dengan nilai", nilai)
    else:
        print("Maaf, Anda tidak lulus dengan nilai", nilai)
else:
    print("Nilai tidak valid. Masukkan nilai antara 0 hingga 100.")
# ==========================================================================================
# TRACE TABLE
# ==========================================================================================
# | Input | Rentang 0-100? | Kondisi Terpenuhi | Nilai Huruf | Output Layar              |
# |-------|----------------|-------------------|-------------|---------------------------|
# | 105   | False          | -                 | -           | Nilai tidak valid...      |
# |  80   | True           | nilai >= 80       | A           | Selamat, lulus nilai A... |
# |  79   | True           | nilai >= 70       | B           | Selamat, lulus nilai B... |
# |  60   | True           | nilai >= 60       | C           | Selamat, lulus nilai C... |
# |  59   | True           | else              | D           | Maaf, tidak lulus nilai D |
# ==========================================================================================