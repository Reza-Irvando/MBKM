#Insertion Sort

def insertionsort(daftar):
    for i in range(1, len(daftar)):
        key = daftar[i]
        j=i-1
        while j>= 0 and key<daftar[j]:
            daftar[j+1] = daftar[j]
            j -= 1
            daftar[j+1]=key

daftar = [7,2,9,5,8,1,6]
print("Data Awal : \n", daftar)
insertionsort(daftar)

akhir = []
for i in range(len(daftar)):
    akhir.append(daftar[i])

print("Data Akhir : \n", akhir)