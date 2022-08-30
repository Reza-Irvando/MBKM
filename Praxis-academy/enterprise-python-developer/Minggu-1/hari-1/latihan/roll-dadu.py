import random

min_val = 1
max_val = 6

a = int(input("Ingin roll dadu? (1 untuk ya / 0 untuk tidak) : "))

while a == 1:
    print("Sedang roll dadu...")
    print("Hasil roll dadu :")
    print(random.randint(min_val, max_val))
    print(random.randint(min_val, max_val))
    a = int(input("Ingin roll dadu? (1 untuk ya / 0 untuk tidak) : "))

print("Selesai")