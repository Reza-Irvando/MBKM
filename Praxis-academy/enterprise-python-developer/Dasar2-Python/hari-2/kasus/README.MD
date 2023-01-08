# Kode Program Python Algoritma Sort
## Quick Sort
### Kode Program:
```
#Quick Sort
def partition(l, r, nums):
	pivot, ptr = nums[r], l
	for i in range(l, r):
		if nums[i] <= pivot:
			nums[i], nums[ptr] = nums[ptr], nums[i]
			ptr += 1
	nums[ptr], nums[r] = nums[r], nums[ptr]
	return ptr

def quicksort(l, r, nums):
	if len(nums) == 1: 
		return nums
	if l < r:
		pi = partition(l, r, nums)
		quicksort(l, pi-1, nums) 
		quicksort(pi+1, r, nums) 
	return nums

example = [4, 5, 1, 2, 3]
print("Data Awal : \n", example)
print("Data Akhir : \n", quicksort(0, len(example)-1, example))

example = [2, 5, 6, 1, 4, 6, 2, 4, 7, 8]
print("Data Awal : \n", example)
print("Data Akhir : \n", quicksort(0, len(example)-1, example))
```

### Hasil Program:
```
Data Awal : 
 [4, 5, 1, 2, 3]
Data Akhir :
 [1, 2, 3, 4, 5]
Data Awal :
 [2, 5, 6, 1, 4, 6, 2, 4, 7, 8]
Data Akhir :
 [1, 2, 2, 4, 4, 5, 6, 6, 7, 8]
```

## Bubble Sort
### Kode Program:
```
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
```

### Hasil Program:
```
Data awal : 
 [30, 50, 40, 80, 60, 10, 20]
Data Akhir :
 [10, 20, 30, 40, 50, 60, 80]
```

## Selection Sort
### Kode Program:
```
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
```

### Hasil Program:
```
Banyak angka : 5
Masukkan angka :
8
5
2
9
4
Data Awal : 
 [8, 5, 2, 9, 4]
Data Akhir :
 [2, 4, 5, 8, 9]
```

## Insertion Sort:
### Kode Program:
```
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
```

### Hasil Program:
```
Data Awal : 
 [7, 2, 9, 5, 8, 1, 6]
Data Akhir :
 [1, 2, 5, 6, 7, 8, 9]
```