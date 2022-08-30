## Hari 2
### More on Lists
# More on Lists

from tkinter import Y


a = fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print("Total : ", a)
b = fruits.count("apple"), " Apple"
print(a, " Apple")
c = fruits.count("starfruit"), "Starfruit"
print(c, " Starfruit")
d = fruits.index("banana", 4) 
print(d, " Banana")
fruits.reverse()
print("Fruits reverse : \n", fruits)
fruits.append("grape")
print("Fruits append : \n", fruits)
fruits.sort()
print("Fruits sort: \n", fruits)
print("Fruits pop : \n", fruits.pop())

### Using Lists as Stack
# Using Lists as Stack

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print("Stack : ", stack)
print("Stack pop : ", stack.pop())
print("Stack : ", stack)
print("Stack pop : ", stack.pop())
print("Stack pop : ", stack.pop())
print("Stack : ", stack)

### List Comprehensions
# List Comprehensions

squares1 = []
for x in range(10):
    squares1.append(x**2)

print("Squares1 : \n", squares1)
squares2 = list(map(lambda x: x**2, range(10)))
print("Squares2 : \n", squares2)
squares3 = [x**2 for x in range(10)]
print("Squares3 : \n", squares3)

print("Combs1 : \n", [(x,y) for x in [1, 2, 3] for y in [3,1,4] if x != y])

combs2 = []
for x in [1, 2, 3]:
    for y in [3,1,4]:
        if x != y:
            combs2.append((x,y))

print("Combs2 : \n", combs2)

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

print("Transposed1 : \n", [[row[i]for row in matrix]for i in range (4)])

transposed2 = []
for i in range (4):
    transposed2.append([row[i]for row in matrix])

print("Transposed2 : \n", transposed2 )

transposed3 = []
for i in range(4):
    transposed3_row = []
    for row in matrix:
        transposed3_row.append(row[i])
    transposed3.append(transposed3_row)

print("Transposed3 : \n", transposed3)

print("Transposed4 : \n", list(zip(*matrix)))

### The del statement
# The del statement

a = [-1, 1, 66.25, 333, 333, 1234.5]
print("a1 : \n", a)
del a[0]
print("a2 : \n", a)
del a[2:4]
print("a3 : \n", a)
del a[:]
print("a4 : \n", a)

### Tuples and Sequences
# Tuples and Sequences

t = 12345, 54321, "hello"
print("t[0] : \n", t[0])
print("t : \n", t)

u = t,(1,2,3,4,5)
print("u : \n", u)

empty = ()
singleton = "hello",
print("len(empty)", len(empty))
print("len(singleton): ", len(singleton))
print("singleton : ", singleton)

### Sets
# Sets
basket = {"apple","orange","apple","pear","orange","banana"}
print("basket : \n", basket)
ril = "orange" in basket
print("'orange' in basket : ", ril)
fek = "crabgrass" in basket
print("'crabgrass' in basket : ", fek)

### Dictionaries
# Dictionaries

tel = {"jack": 4098, "sape": 4139}
tel["guido"] = 4127
print("tel1 : \n", tel)
print("tel['jack'] : ", tel["jack"])
del tel["sape"]
tel["irv"] = 4127
print("tel2 : \n", tel)
print("list tel : \n", list (tel))
print("sorted tel : \n", sorted(tel))
ril2 = "guido" in tel
print("'guido' in tel : ", ril2)
fek2 = "jack" not in tel
print("'jack' not in tel : ", fek2)

### Looping Techniques
# Looping Techniques

knights = {"gallahad":"the pure","robin":"the brave"}
print("Knights : ")
for k, v in knights.items():
    print(k,v)

print("Tic Tac Toe : ")
for i, v in enumerate(["tic", "tac", "toe"]):
    print(i,v)

tanya = ["name", "quest", "favorite color"]
jawab = ["lancelot", "the holy grail", "blue"]
for q, a in zip(tanya, jawab):
    print("What is your{0}? it is {1}.".format(q,a))

print("Reversed range : ")
for i in reversed(range(1, 10, 2)):
    print(i)

basket2 = ["apple","orange", "apple","pear","orange","banana"]
print("basket : \n", basket2)
print("sorted basket :")
for i in sorted(basket):
    print(i)

print("sorted set basket")
for j in sorted(set(basket)):
    print(j)

import math
raw_data = [56.2, float("NaN"), 51.7, 55.3, 52.5, float("NaN"), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print("Filtered Data : \n", filtered_data)