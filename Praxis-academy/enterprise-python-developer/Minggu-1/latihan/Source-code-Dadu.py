#Dadu
import random
#range angka dadu
min_val = 1
max_val = 6

roll_lagi = "ya"
#loop
while roll_lagi == "ya" or roll_lagi == "y":
    print("Sedang Roll Dadu...")
    print("Angka hasil roll : ")
    #roll dadu pertama
    print(random.randint(min_val, max_val))
    #roll dadu kedua
    print(random.randint(min_val, max_val))
    roll_again = input("Roll dadu lagi? (y/t)")
    
