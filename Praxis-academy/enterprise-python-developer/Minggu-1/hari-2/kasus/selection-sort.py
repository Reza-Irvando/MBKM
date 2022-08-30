def selectionsort(daftar, banyak):
    for i in range(banyak):
        min_index = i

        for j in range(i+1, banyak):
            if daftar[j]<daftar[min_index]:
                min_index = j
        (daftar[i], daftar[min_index]) = (daftar[min_index], daftar[i])

daftar = []
banyak = int(input("Banyak angka : "))
print("Masukkan angka :")

for i in range (0, banyak):
    angka = int(input())
    daftar.append(angka)

print("Data Awal : \n", daftar)
selectionsort(daftar, banyak)
print("Data Akhir : \n", daftar)