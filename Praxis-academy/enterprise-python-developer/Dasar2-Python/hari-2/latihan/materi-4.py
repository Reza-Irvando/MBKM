while True print("Hello World")
File"<stdin>, line 1
while True print("Hello World")

10 * (1/0)
Traceback(most recent call last):
File"(stdin)", line 1, in <module>

4 + spam*3
Traceback (most recent call last)
File"<stdin>", line 1, in <module>

"2"+2
Traceback(most recent call last):
File "<stdin>", line 1, in <module>

while True:
    try:
        x = int(input("Please enter a number : "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try Again...."