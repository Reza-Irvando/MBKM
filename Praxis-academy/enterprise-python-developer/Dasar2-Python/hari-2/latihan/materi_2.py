### Save as module_using_sys.py
# Save as module_using_sys.py

import sys
print("The command line arguments are: ")
for i in sys.argv:
    print(i)

print("\n\nThe PYTHON is ", sys.path, "\n")

from math import sqrt
print("Square root of 16 is ", sqrt(16))

if __name__ == "__main__":
    print("This program is being run by itself")
else:
    print("I am being imported from another module")

def say_hi():
    print("Hi, this is mymodule speaking")
__version__ = "0.1"