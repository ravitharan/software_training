# EX:4 2) Write a function to determine a given number is a prime number or not.

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

if check_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
