#Bubble Sort

def bubblesort(data1):
    n = len(data1)
    swap = False
    for i in range (n-1):
        for j in range (n-i-1):
            if data1[j]>data1[j+1]:
                swap = True
                data1[j], data1[j+1] = data1[j+1], data1[j]
            
        if not swap:
            return

data1 = [30, 50, 40, 80, 60, 10, 20]

print("Data awal : \n", data1)
bubblesort(data1)
print("Data Akhir : \n", data1)