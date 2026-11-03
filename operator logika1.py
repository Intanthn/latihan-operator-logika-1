
print("===== PROGRAM NILAI SISWA =====")

nama = input("Masukkan nama siswa: ")
nilai_teori = int(input("Masukkan nilai teori: "))
nilai_praktik = int(input("Masukkan nilai praktik: "))

rata_rata = (nilai_teori + nilai_praktik) / 2

if nilai_teori >= 75 and nilai_praktik >= 75:
    keterangan = "LULUS"
else:
    keterangan = "TIDAK LULUS"

if rata_rata >= 90 or rata_rata == 100:
    predikat = "Sangat Baik"
elif rata_rata >= 80:
    predikat = "Baik"
elif rata_rata >= 75:
    predikat = "Cukup"
else:
    predikat = "Kurang"

print("\n===== HASIL NILAI SISWA =====")
print("Nama Siswa :", nama)
print("Nilai Teori :", nilai_teori)
print("Nilai Praktik :", nilai_praktik)
print("Nilai Rata-rata :", rata_rata)
print("Predikat :", predikat)
print("Keterangan :", keterangan)
