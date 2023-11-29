import math
while True:
    b = int(input("Enter a number (or type 'exit' to end): "))

    if b == 'exit':
        break
    a = int(math.sqrt(b))**2 == b
    if a:
        print("{b} is a square number.")
    else:
        print("{b} is not a square number.")