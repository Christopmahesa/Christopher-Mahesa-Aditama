# Program menentukan kelulusan mahasiswa
nama = (input("nama mahasiswa: "))
UTS = float(input("nilai UTS: "))
UAS = float(input("nilai UAS: "))
absensi = float(input("jumlah absensi: "))
total_nilai = (UTS * 0.2) + (UAS * 0.4) + (absensi * 0.4)
print("nama: ", nama)
print("UTS: ", UTS)
print("UAS: ", UAS)
print("absensi: ", absensi)
print("nilai akhir: ", total_nilai)
#pengelompokan nilai
if total_nilai >= 90:
    print("grade: A")
elif total_nilai >= 80:
    print("grade: B")
elif total_nilai >= 70:
    print("grade: C")
elif total_nilai >= 50:
    print("grade: D")
elif total_nilai <= 40:
    print("grade: E")

if total_nilai >= 60:
    print("keterangan: lulus")
else:
    print("keterangan: tidak lulus")
