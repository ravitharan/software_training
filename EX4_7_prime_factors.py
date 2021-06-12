# EX:6 1) Find prime factors of a number.

import sys

if len(sys.argv) != 2:
    print(f"Argument error\n Usage {sys.argv[0]} <number>")
    exit(1)

number = int(sys.argv[1])

factors = []
factor = 2
while (number >= factor):
    while ((number % factor) == 0):
        factors.append(factor)
        number = number // factor
    factor += 1

print(factors)
