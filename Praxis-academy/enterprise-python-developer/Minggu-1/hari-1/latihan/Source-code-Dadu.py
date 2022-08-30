#Dadu
import random

roll = input("Ingin roll dadu? (y/t) ")

if (roll == y):
    min_val = 1
    max_val = 6
    print("Sedang roll dadu...")
    print("Angka hasil roll : ")
    print(random.randint(min_val, max_val))
    print(random.randint(min_val, max_val))

roll_lagi = input("Ingin roll lagi? (y/t)")

if (roll_lagi == y):
    min_val = 1
    max_val = 6
    print("Sedang roll dadu...")
    print("Angka hasil roll : ")
    print(random.randint(min_val, max_val))
    print(random.randint(min_val, max_val))

if (roll_lagi == 0):
    print("selese")
