# # EX:4 6) Create 100 random numbers between 1 to 100 and group every number into bins
# with intervals of 10. Eg bins are 1-10, 11-20,..91-100.

import sys

def check_prime(number): 
    is_prime = True

    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
    return is_prime

if len(sys.argv) != 2:
    print(f"Argument error\n Usage {sys.argv[0]} <number>")
    exit(1)

number = int(sys.argv[1])

factors = []
while number > 1:
    for prime in range(2, number):




