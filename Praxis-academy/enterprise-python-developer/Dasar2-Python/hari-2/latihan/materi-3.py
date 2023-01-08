s = "Hello, world"
str(s)
repr(s)
str(1/7)
x = 10 * 3.25
y = 200 * 200
s = "The value of x is " + repr(x) + ", and y is " + repr(y) + "..."
print(s)
hello = "hello, world\n"
hellos = repr(hello)
print(hellos)
print(repr((x, y, ("spam", "eggs"))))

import math
print(f" The value of pi is approximately {math.pi:.3f}.")

table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 7678}
for name, phone in table.items():
    print(f"{name:10}==>{phone:10d}")

animals = "eels"
print(f"My hovercraft is full of {animals}.")
print(f"My hovercraft is full of {animals!r}.")

print("This {food} is {adjective}.".format(
    food = "spam", adjective = "absolutely horrible"))

print("The story of {0}, {1}, and {other}.".format("Bill", "Manfred", other = "Georg"))

table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 863156}
print("Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; "
        "Dcab: {0[Dcab]:d}".format(table))

table = {"Sjoerd": 4127, "Jack": 4098,"Dcab":8617242}
print("Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}".format(**table))

for x in range(1,11):
    print("{0:2d} {1:3d} {2:4d}".format(x, x*x, x*x*x))

for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=" ")
    print(repr(x*x*x).rjust(4))

print("12".zfill(5))
print("-3.14".zfill(7))
print("3.14159265359".zfill(5))

import math
print("The value of pi is approximately %5.3f." % math.pi)

import json
x = [1, "simple", "list"]
print(json.dumps(x))
