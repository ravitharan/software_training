# EX:4 6) Write function to return number of vowels of a string

import sys

if len(sys.argv) != 2:
    print(f"Argument error\n number of arguments {len(sys.argv)}, expected 2")
    print(f" Usage: {sys.argv[0]} <input_string>")
    exit(1)

VOWELS = "aeiouAEIOU"

input_string = sys.argv[1]

num_vowels = 0

for char in input_string:
    if char in VOWELS:
        num_vowels += 1

print(f"Number of vewels in \"{input_string}\" is {num_vowels}")
