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
